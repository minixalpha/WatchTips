/* CREATE USER 'proj'@'localhost' IDENTIFIED BY 'XXX'; */
/* GRANT SELECT, INSERT, UPDATE, DELETE ON *.* to 'proj'@'localhost'; */
/* CREATE DATABASE watchtips CHARACTER SET UTF8; */

USE watchtips;

CREATE TABLE `wt_user` (
    `user_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
    `user_name` TEXT NOT NULL,
    `user_password` TEXT NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `wt_category` (
    `category_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
    `category_name` TEXT NOT NULL,
    `user_id` BIGINT(20) NOT NULL,
    PRIMARY KEY (`category_id`),
    FOREIGN KEY (user_id)
    REFERENCES wt_user(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `wt_tips` (
    `tips_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
    `tips_title` TEXT,
    `tips_content` LONGTEXT,
    `category_id` BIGINT(20),
    PRIMARY KEY (`tips_id`),
    FOREIGN KEY (category_id)
    REFERENCES wt_category(category_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
