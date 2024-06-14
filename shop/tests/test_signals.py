from django.test import TestCase
from shop import models
from django.core.files.images import ImageFile
from decimal import Decimal


class TestSignal(TestCase):
    def testThumbnailsAreGeneratedOnSave(self):
        
        product = models.Product(
                name="Test Product for testing Thumbnails",
                price=Decimal("10.00"),
                ) 
        product.save()

        
        with open("modernman/fixtures/test_thumbnail.jpg", "rb" ) as file:
            image = models.ProductImage(
                product=product,
                image=ImageFile(file, name="test_thumbnail.jpg"),
                )

            with self.assertLogs("main", level="INFO") as cm:
                image.save()
            
            # confirm an image thumbnail has been generated
            self.assertGreaterEqual(len(cm.output), 1)
            image.refresh_from_db()

        with open("modernman/fixtures/test_thumbnail.jpg", "rb",) as file:
            expected_content = file.read()

        # confirm thumbnail contents match
        assert image.thumbnail.read() == expected_content
        
        # delete the test thumbnail image
        image.thumbnail.delete(save=False)
        image.image.delete(save=False)





