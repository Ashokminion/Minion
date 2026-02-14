package com.recommendation.controller;

import com.recommendation.entity.Item;
import com.recommendation.service.RecommendationService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/recommendations")
@RequiredArgsConstructor
public class RecommendationController {

    private final RecommendationService recommendationService;

    @GetMapping
    public ResponseEntity<List<Item>> getRecommendations(@AuthenticationPrincipal UserDetails userDetails) {
        List<Item> recommendations = recommendationService.getRecommendations(userDetails.getUsername());
        return ResponseEntity.ok(recommendations);
    }
}
