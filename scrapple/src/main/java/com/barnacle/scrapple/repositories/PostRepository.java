package com.barnacle.scrapple.repositories;

import com.barnacle.scrapple.domain.Post;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepository extends JpaRepository<Post, Integer> {
}
