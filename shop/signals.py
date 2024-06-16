from io import BytesIO
import logging
from PIL import Image
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductImage


THUMBNAIL_SIZE = (300, 300)
logger = logging.getLogger(__name__)


@receiver(pre_save, sender=ProductImage)
def generate_thumbnail(sender, instance, **kwargs):

    logger.info( f"Generating thumbnail for {instance.product.name}  product id: {instance.product.id}" )

    image = Image.open(instance.image)
    image = image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)

    temp_thumb = BytesIO()

    image.save(temp_thumb, "PNG")
    
    temp_thumb.seek(0)

  
    # set save=False, otherwise it will run in an infinite loop
    instance.thumbnail.save(
        instance.image.name,
        ContentFile(
            temp_thumb.read()),
            save=False,
            )
    
    temp_thumb.close()
    
    
    