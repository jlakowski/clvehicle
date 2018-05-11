CREATE TABLE `jeep_wrangler` 
(  `id` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `VIN` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Year` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `condition` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cylinders` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `drive` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL,
  `fuel` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `geotag` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `has_image` tinyint(1) DEFAULT NULL,
  `has_map` tinyint(1) DEFAULT NULL,
  `location` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `make` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `model` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `odometer` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `paint color` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `repost_of` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `size` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `title status` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `transmission` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `where` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `ix_craigslist_jeep_wrangler_id` (`id`)
  ) 
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 
  COLLATE=utf8mb4_unicode_ci

