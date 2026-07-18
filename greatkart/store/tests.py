from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from category.models import Category
from store.models import Product


class ProductDetailViewTests(TestCase):
    def test_product_detail_displays_product_name(self):
        category = Category.objects.create(
            category_name='Shoes',
            slug='shoes',
            description='Sport shoes',
        )
        product = Product.objects.create(
            product_name='Nike Air',
            slug='nike-air',
            description='Great shoes',
            price=100,
            images=SimpleUploadedFile(
                'nike.jpg',
                b'fake-image-content',
                content_type='image/jpeg',
            ),
            stock=10,
            is_available=True,
            category=category,
        )

        response = self.client.get(
            reverse('product_detail', kwargs={
                'category_slug': category.slug,
                'product_slug': product.slug,
            })
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.product_name)
