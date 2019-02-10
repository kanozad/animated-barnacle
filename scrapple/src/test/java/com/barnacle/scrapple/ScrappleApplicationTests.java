package com.barnacle.scrapple;

import com.barnacle.scrapple.domain.Post;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.Date;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
public class ScrappleApplicationTests {

    Logger log = LoggerFactory.getLogger(ScrappleApplicationTests.class);

    private static final String ROOT_URL = "http://localhost:8080";
    RestTemplate restTemplate = new RestTemplate();

    @Test
    public void contextLoads() {
    }

    @Test
    public void testGetAllPosts() {
        ResponseEntity<Post[]> responseEntity = restTemplate.getForEntity(ROOT_URL + "/posts", Post[].class);
        List<Post> posts = Arrays.asList(responseEntity.getBody());
        log.debug("{}", posts);

        assertNotNull(posts);
    }

    @Test
    public void testCreatePost() {
        Post post = new  Post();
        post.setTitle("Lorem ipsum dolor sit amet");
        post.setContent("Lorem ipsum dolor sit amet");
        post.setCreatedOn(new Date());
        ResponseEntity<Post> postResponse = restTemplate.postForEntity(ROOT_URL + "/posts", post, Post.class);
        assertNotNull(postResponse);
        assertNotNull(postResponse.getBody());
    }
}

