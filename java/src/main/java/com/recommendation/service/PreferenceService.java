package com.recommendation.service;

import com.recommendation.entity.Preference;
import com.recommendation.entity.User;
import com.recommendation.repository.PreferenceRepository;
import com.recommendation.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class PreferenceService {

    private final PreferenceRepository preferenceRepository;
    private final UserRepository userRepository;

    public Preference addPreference(String username, String category, Double weight) {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        Preference preference = new Preference();
        preference.setUser(user);
        preference.setCategory(category);
        preference.setWeight(weight);

        return preferenceRepository.save(preference);
    }

    public List<Preference> getUserPreferences(String username) {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        return preferenceRepository.findByUserId(user.getId());
    }
}
