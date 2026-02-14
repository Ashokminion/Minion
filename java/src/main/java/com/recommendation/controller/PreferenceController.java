package com.recommendation.controller;

import com.recommendation.entity.Preference;
import com.recommendation.service.PreferenceService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/preferences")
@RequiredArgsConstructor
public class PreferenceController {

    private final PreferenceService preferenceService;

    @GetMapping
    public ResponseEntity<List<Preference>> getPreferences(@AuthenticationPrincipal UserDetails userDetails) {
        List<Preference> preferences = preferenceService.getUserPreferences(userDetails.getUsername());
        return ResponseEntity.ok(preferences);
    }

    @PostMapping
    public ResponseEntity<Preference> addPreference(
            @AuthenticationPrincipal UserDetails userDetails,
            @RequestBody Map<String, Object> request) {

        String category = (String) request.get("category");
        Double weight = request.containsKey("weight") ? Double.valueOf(request.get("weight").toString()) : 1.0;

        Preference preference = preferenceService.addPreference(
                userDetails.getUsername(),
                category,
                weight);

        return ResponseEntity.ok(preference);
    }
}
