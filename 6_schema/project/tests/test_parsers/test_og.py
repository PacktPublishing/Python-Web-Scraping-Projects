from schema.parsers.opengraph import format_og


def test_format_og():
    data = {
        "namespace": {"og": "http://ogp.me/ns#"},
        "properties": [
            ("og:description",
             "Free Shipping on orders over $35. Buy Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks) at Walmart.com"),
            ("og:image",
             "https://i5.walmartimages.com/asr/ce1033ea-4934-4098-af07-16d0136689fd_1.5cebe0dbf47d95ddc489e506c8cc28f7.jpeg"),
            ("og:url",
             "/ip/Dungeons-Dragons-Player-s-Handbook-Dungeons-Dragons-Core-Rulebooks-9780786965601/37784457"),
            ("og:title",
             "Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks) - Walmart.com"),
            ("og:site_name", "Walmart.com"),
            ("og:type", "product.item"),
        ],
    }
    expected = {
        "description": "Free Shipping on orders over $35. Buy Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks) at Walmart.com",
        "image": "https://i5.walmartimages.com/asr/ce1033ea-4934-4098-af07-16d0136689fd_1.5cebe0dbf47d95ddc489e506c8cc28f7.jpeg",
        "type": "product.item",
        "url": "/ip/Dungeons-Dragons-Player-s-Handbook-Dungeons-Dragons-Core-Rulebooks-9780786965601/37784457",
        "site_name": "Walmart.com",
        "title": "Dungeons & Dragons Player's Handbook (Dungeons & Dragons Core Rulebooks) - Walmart.com",
    }
    assert format_og(data) == expected
