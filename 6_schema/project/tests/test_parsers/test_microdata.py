from schema.parsers.microdata import format_microdata


def test_microdata():
    data = [
        {
            "type": "http://schema.org/Product",
            "properties": {
                "image": "https://i5.walmartimages.com/asr/ce1033ea-4934-4098-af07-16d0136689fd_1.5cebe0dbf47d95ddc489e506c8cc28f7.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
                "name": [
                    "Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks)",
                    "",
                ],
                "sku": "37784457",
                "aggregateRating": {
                    "type": "//schema.org/AggregateRating",
                    "properties": {
                        "ratingValue": "4.8",
                        "bestRating": "5",
                        "reviewCount": "32",
                    },
                },
                "brand": "Wizards RPG Team",
                "offers": {
                    "type": "//schema.org/Offer",
                    "properties": {
                        "url": "/ip/Dungeons-Dragons-Player-s-Handbook-Dungeons-Dragons-Core-Rulebooks-9780786965601/37784457",
                        "priceValidUntil": "",
                        "priceCurrency": "USD",
                        "price": "27.11",
                        "availability": "//schema.org/InStock",
                        "itemCondition": "//schema.org/NewCondition",
                        "availableDeliveryMethod": "//schema.org/OnSitePickup",
                        "availableAtOrFrom": {
                            "type": "//schema.org/Place",
                            "properties": {
                                "name": "San Leandro Store",
                                "branchCode": "2648",
                            },
                        },
                    },
                },
                "review": [
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "author": {"type": "http://schema.org/Person", "value": ""}
                        },
                    },
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "name": "Can't believe it!! :D",
                            "reviewRating": {
                                "type": "//schema.org/Rating",
                                "properties": {
                                    "worstRating": "1",
                                    "ratingValue": "5",
                                    "bestRating": "5",
                                },
                            },
                            "reviewBody": "I've been thinking of getting the Player's Handbook for a while now, but I always felt like it was too much for me to spend.. until I found this!! It's the same book, fully licenses and hard cover, but for a fraction of the price (and it came two days early!). Believe me, I was hesitant at first, but it's the real deal. Anyways.. hope all of y'all have a great day!See more",
                            "author": "Liz,",
                            "datePublished": "February 9, 2019",
                        },
                    },
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "name": "Hardcore Hard Cover Awesome!",
                            "reviewRating": {
                                "type": "//schema.org/Rating",
                                "properties": {
                                    "worstRating": "1",
                                    "ratingValue": "5",
                                    "bestRating": "5",
                                },
                            },
                            "reviewBody": "The purchase experience was easy. Found exactly what I was looking for online and the free in store pick up was a breeze! The book itself is awesome! The art is GORGEOUS and the details are easy to understand. The book is pretty heavy though so I wouldn't suggest dropping it on your foot. Speaking from experience. Giggle.See more",
                            "author": "AskinYoheC,",
                            "datePublished": "March 1, 2017",
                        },
                    },
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "name": "New Edition of Player Rules.",
                            "reviewRating": {
                                "type": "//schema.org/Rating",
                                "properties": {
                                    "worstRating": "1",
                                    "ratingValue": "5",
                                    "bestRating": "5",
                                },
                            },
                            "reviewBody": "Adds some new races and a new class. Great advantage/disadvantage feature. Same ole' D&D but better. Highly recommend for the newbie or veteran. NEEDED TO PLAY THE GAME EFFECTIVELYSee more",
                            "author": "zngraceland,",
                            "datePublished": "October 7, 2014",
                        },
                    },
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "name": "Exactly what I expected!",
                            "reviewRating": {
                                "type": "//schema.org/Rating",
                                "properties": {
                                    "worstRating": "1",
                                    "ratingValue": "5",
                                    "bestRating": "5",
                                },
                            },
                            "reviewBody": "It was shipped much quicker than I thought it would be and the product was exactly what I thought it would be!See more",
                            "author": "hbg6044,",
                            "datePublished": "October 26, 2014",
                        },
                    },
                    {
                        "type": "http://schema.org/Review",
                        "properties": {
                            "name": "Perfect condition",
                            "reviewRating": {
                                "type": "//schema.org/Rating",
                                "properties": {
                                    "worstRating": "1",
                                    "ratingValue": "5",
                                    "bestRating": "5",
                                },
                            },
                            "reviewBody": "Arrived well-packed and sooner than expectedSee more",
                            "author": "DnD4U,",
                            "datePublished": "September 13, 2016",
                        },
                    },
                ],
                "description": "Hardback: Dungeons &amp; Dragons Player's Handbook (Dungeons &amp; Dragons Core Rulebooks)",
            },
        },
        {
            "type": "//schema.org/BreadcrumbList",
            "properties": {
                "itemListElement": [
                    {
                        "type": "//schema.org/ListItem",
                        "properties": {
                            "item": {
                                "type": "//schema.org/Thing",
                                "id": "//www.walmart.com/cp/3920",
                                "properties": {"name": "Books"},
                            },
                            "position": "1",
                        },
                    },
                    {
                        "type": "//schema.org/ListItem",
                        "properties": {
                            "item": {
                                "type": "//schema.org/Thing",
                                "id": "//www.walmart.com/cp/582361",
                                "properties": {"name": "Crafts & Hobbies Books"},
                            },
                            "position": "2",
                        },
                    },
                    {
                        "type": "//schema.org/ListItem",
                        "properties": {
                            "item": {
                                "type": "//schema.org/Thing",
                                "id": "//www.walmart.com/cp/9999446",
                                "properties": {"name": "Game & Activity Books"},
                            },
                            "position": "3",
                        },
                    },
                    {
                        "type": "//schema.org/ListItem",
                        "properties": {
                            "item": {
                                "type": "//schema.org/Thing",
                                "id": "//www.walmart.com/cp/4085188",
                                "properties": {"name": "Role Playing & Fantasy Books"},
                            },
                            "position": "4",
                        },
                    },
                ]
            },
        },
    ]
    expected = [
        {
            "image": "https://i5.walmartimages.com/asr/ce1033ea-4934-4098-af07-16d0136689fd_1.5cebe0dbf47d95ddc489e506c8cc28f7.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
            "name": [
                "Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks)",
                "",
            ],
            "sku": "37784457",
            "aggregateRating": {
                "ratingValue": "4.8",
                "bestRating": "5",
                "reviewCount": "32",
                "type": "//schema.org/AggregateRating",
            },
            "brand": "Wizards RPG Team",
            "offers": {
                "url": "/ip/Dungeons-Dragons-Player-s-Handbook-Dungeons-Dragons-Core-Rulebooks-9780786965601/37784457",
                "priceValidUntil": "",
                "priceCurrency": "USD",
                "price": "27.11",
                "availability": "//schema.org/InStock",
                "itemCondition": "//schema.org/NewCondition",
                "availableDeliveryMethod": "//schema.org/OnSitePickup",
                "availableAtOrFrom": {
                    "name": "San Leandro Store",
                    "branchCode": "2648",
                    "type": "//schema.org/Place",
                },
                "type": "//schema.org/Offer",
            },
            "review": [
                {
                    "author": {"type": "http://schema.org/Person", "value": ""},
                    "type": "http://schema.org/Review",
                },
                {
                    "name": "Can't believe it!! :D",
                    "reviewRating": {
                        "worstRating": "1",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "type": "//schema.org/Rating",
                    },
                    "reviewBody": "I've been thinking of getting the Player's Handbook for a while now, but I always felt like it was too much for me to spend.. until I found this!! It's the same book, fully licenses and hard cover, but for a fraction of the price (and it came two days early!). Believe me, I was hesitant at first, but it's the real deal. Anyways.. hope all of y'all have a great day!See more",
                    "author": "Liz,",
                    "datePublished": "February 9, 2019",
                    "type": "http://schema.org/Review",
                },
                {
                    "name": "Hardcore Hard Cover Awesome!",
                    "reviewRating": {
                        "worstRating": "1",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "type": "//schema.org/Rating",
                    },
                    "reviewBody": "The purchase experience was easy. Found exactly what I was looking for online and the free in store pick up was a breeze! The book itself is awesome! The art is GORGEOUS and the details are easy to understand. The book is pretty heavy though so I wouldn't suggest dropping it on your foot. Speaking from experience. Giggle.See more",
                    "author": "AskinYoheC,",
                    "datePublished": "March 1, 2017",
                    "type": "http://schema.org/Review",
                },
                {
                    "name": "New Edition of Player Rules.",
                    "reviewRating": {
                        "worstRating": "1",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "type": "//schema.org/Rating",
                    },
                    "reviewBody": "Adds some new races and a new class. Great advantage/disadvantage feature. Same ole' D&D but better. Highly recommend for the newbie or veteran. NEEDED TO PLAY THE GAME EFFECTIVELYSee more",
                    "author": "zngraceland,",
                    "datePublished": "October 7, 2014",
                    "type": "http://schema.org/Review",
                },
                {
                    "name": "Exactly what I expected!",
                    "reviewRating": {
                        "worstRating": "1",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "type": "//schema.org/Rating",
                    },
                    "reviewBody": "It was shipped much quicker than I thought it would be and the product was exactly what I thought it would be!See more",
                    "author": "hbg6044,",
                    "datePublished": "October 26, 2014",
                    "type": "http://schema.org/Review",
                },
                {
                    "name": "Perfect condition",
                    "reviewRating": {
                        "worstRating": "1",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "type": "//schema.org/Rating",
                    },
                    "reviewBody": "Arrived well-packed and sooner than expectedSee more",
                    "author": "DnD4U,",
                    "datePublished": "September 13, 2016",
                    "type": "http://schema.org/Review",
                },
            ],
            "description": "Hardback: Dungeons &amp; Dragons Player's Handbook (Dungeons &amp; Dragons Core Rulebooks)",
            "type": "http://schema.org/Product",
        },
        {
            "//schema.org/BreadcrumbList": [
                {
                    "item": {"name": "Books", "type": "//schema.org/Thing"},
                    "position": "1",
                    "type": "//schema.org/ListItem",
                },
                {
                    "item": {
                        "name": "Crafts & Hobbies Books",
                        "type": "//schema.org/Thing",
                    },
                    "position": "2",
                    "type": "//schema.org/ListItem",
                },
                {
                    "item": {
                        "name": "Game & Activity Books",
                        "type": "//schema.org/Thing",
                    },
                    "position": "3",
                    "type": "//schema.org/ListItem",
                },
                {
                    "item": {
                        "name": "Role Playing & Fantasy Books",
                        "type": "//schema.org/Thing",
                    },
                    "position": "4",
                    "type": "//schema.org/ListItem",
                },
            ]
        },
    ]
    for i, d in enumerate(data):
        assert format_microdata(d) == expected[i]


if __name__ == "__main__":
    test_microdata()
