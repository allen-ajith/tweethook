<?php
create_user_table = 'CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `twitter_handle` varchar(100) NOT NULL,
  `password` varchar(250) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;';

