package com.barnacle.scrapple.repositories;

import com.barnacle.scrapple.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Integer> {
}
