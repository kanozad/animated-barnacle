package com.pirate.broccoli.earwax;

import de.codecentric.boot.admin.server.config.EnableAdminServer;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableAdminServer
public class EarwaxApplication {

    public static void main(String[] args) {
        SpringApplication.run(EarwaxApplication.class, args);
    }

}
