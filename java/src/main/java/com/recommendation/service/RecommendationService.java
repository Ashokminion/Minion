package com.recommendation.service;

import com.recommendation.entity.Item;
import com.recommendation.entity.Preference;
import com.recommendation.entity.User;
import com.recommendation.repository.PreferenceRepository;
import com.recommendation.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.*;

@Service
@RequiredArgsConstructor
public class RecommendationService {

    private final UserRepository userRepository;
    private final PreferenceRepository preferenceRepository;
    private final ItemService itemService;
    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${ai.service.url}")
    private String aiServiceUrl;

    public List<Item> getRecommendations(String username) {
        // Get user and preferences
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        List<Preference> preferences = preferenceRepository.findByUserId(user.getId());

        // Build user profile for AI service
        Map<String, Object> userProfile = new HashMap<>();
        userProfile.put("user_id", user.getId());

        List<String> categories = preferences.stream()
                .map(Preference::getCategory)
                .toList();
        userProfile.put("categories", categories);

        // Get all items to send to AI
        List<Item> allItems = itemService.getAllItems();
        List<Map<String, Object>> itemsList = allItems.stream()
                .map(item -> {
                    Map<String, Object> itemMap = new HashMap<>();
                    itemMap.put("id", item.getId());
                    itemMap.put("title", item.getTitle());
                    itemMap.put("category", item.getCategory());
                    itemMap.put("tags", item.getTags());
                    return itemMap;
                })
                .toList();

        Map<String, Object> requestBody = new HashMap<>();
        requestBody.put("user_profile", userProfile);
        requestBody.put("items", itemsList);

        try {
            // Call Flask AI service
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<Map<String, Object>> request = new HttpEntity<>(requestBody, headers);

            @SuppressWarnings("unchecked")
            Map<String, Object> response = restTemplate.postForObject(
                    aiServiceUrl + "/recommend",
                    request,
                    Map.class);

            if (response != null && response.containsKey("recommended_items")) {
                @SuppressWarnings("unchecked")
                List<Integer> recommendedIds = (List<Integer>) response.get("recommended_items");

                List<Long> ids = recommendedIds.stream()
                        .map(Long::valueOf)
                        .toList();

                return itemService.getItemsByIds(ids);
            }
        } catch (Exception e) {
            // Fallback: return random items if AI service is unavailable
            Collections.shuffle(allItems);
            return allItems.stream().limit(5).toList();
        }

        return new ArrayList<>();
    }
}
