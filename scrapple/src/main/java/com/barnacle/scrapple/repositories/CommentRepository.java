package com.barnacle.scrapple.repositories;

import com.barnacle.scrapple.domain.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CommentRepository extends JpaRepository<Comment, Integer> {
}
