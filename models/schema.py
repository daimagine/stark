from marshmallow import Schema, fields, pprint

"""
Socmed Schemas
"""
class SocialMediaSchema(Schema):
    class Meta:
        fields = (
            'id', 
            'name',
        )


class CustomerSocmedAccountSchema(Schema):
    social_media = fields.Nested(SocialMediaSchema)
    class Meta:
        fields = (
            'id', 
            'social_id', 
            'social_name',
            'image',
            'type',
            'social_media'
        )


"""
Customer Schemas
"""
class CustomerSchema(Schema):
    socmed_accounts = fields.Nested(CustomerSocmedAccountSchema, many=True)
    class Meta:
        fields = (
            'id', 
            'name', 
            'email', 
            'mobile_no',
            'phone_1',
            'phone_2',
            'phone_3',
            'address',
            'bank_account_no',
            'bank_account_name',
            'bank_name',
            'email_verified',
            'phone_verified',
            'socmed_accounts'
        )


class CustomerAuthSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'client_token', 'client_token_valid_time') 


"""
Affiliate Customer Schema
"""
class AffiliateCustomerSchema(Schema):
    customer = fields.Nested(CustomerSchema)
    class Meta:
        fields = ('id', 'customer')


"""
Product Images Schema
"""
class ProductImagesSchema(Schema):
    class Meta:
        fields = (
            'id', 
            'link', 
            'is_primary'
        )


"""
Product Category Schema
"""
class CategorySchema(Schema):
    class Meta:
        fields = (
            'id', 
            'name', 
            'description', 
            'need_logistic', 
            'downloadable', 
            'stock_related', 
            'have_expiry_date'
        )


"""
Product Schemas
"""
class ProductSchema(Schema):
    category = fields.Nested(CategorySchema)
    customer = fields.Nested(CustomerSchema)
    affiliates = fields.Nested(AffiliateCustomerSchema, many=True)
    product_images = fields.Nested(ProductImagesSchema, many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'token',
            'price',
            'is_affiliate_ready',
            'affiliate_percentage',
            'affiliate_fee',
            'affiliate_fee_type',
            'customer',
            'affiliates',
            'image',
            'description',
            'headline',
            'product_page',
            'category',
            'product_images'
        )


"""
Affiliate Schema
"""
class AffiliateSchema(Schema):
    product = fields.Nested(ProductSchema)
    customer = fields.Nested(CustomerSchema)
    class Meta:
        fields = ('id', 'product', 'customer', 'headline', 'product_page')


class AffiliateInfoSchema(Schema):
    class Meta:
        fields = ('id', 'product_id', 'customer_id', 'headline', 'product_page')