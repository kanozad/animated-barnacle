package com.barnacle.scrapple.controllers;

import com.barnacle.scrapple.domain.Comment;
import com.barnacle.scrapple.domain.Post;
import com.barnacle.scrapple.exceptions.ResourceNotFoundException;
import com.barnacle.scrapple.repositories.CommentRepository;
import com.barnacle.scrapple.repositories.PostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/posts")
public class PostController {

    @Autowired
    PostRepository postRepository;

    @Autowired
    CommentRepository commentRepository;

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping(value = "")
    public Post createPost(@RequestBody Post post) {
        return postRepository.save(post);
    }

    @GetMapping(value = "")
    public List<Post> listPosts() {
        return postRepository.findAll();
    }

    @GetMapping(value = "/{id}")
    public Post getPost(@PathVariable("id") Integer id) {
        return postRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("No post found with id=" + id));
    }

    @PutMapping(value = "/{id}")
    public Post updatePost(@PathVariable("id") Integer id, @RequestBody Post post) {
        postRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("No post found with id=" + id));
        return postRepository.save(post);
    }

    @DeleteMapping(value = "/{id}")
    public void deletePost(@PathVariable("id") Integer id) {
        Post post = postRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("No post found with id=" + id));
        postRepository.deleteById(post.getId());
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("/{id}/comments")
    public void createPostComment(@PathVariable("id") Integer id, @RequestBody Comment comment) {
        Post post = postRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("No post found with id=" + id));
        post.getComments().add(comment);
    }

    @DeleteMapping("/{postId}/comments/{commentId}")
    public void deletePostComment(@PathVariable("postId") Integer postId, @PathVariable("commentId") Integer commentId) {
        commentRepository.deleteById(commentId);
    }


}
