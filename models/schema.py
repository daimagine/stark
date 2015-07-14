from marshmallow import Schema, fields, pprint


"""
Customer Schemas
"""
class CustomerSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email')

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
Product Schemas
"""
class ProductSchema(Schema):
    customer = fields.Nested(CustomerSchema)
    affiliates = fields.Nested(AffiliateCustomerSchema, many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'is_affiliate_ready',
            'affiliate_percentage',
            'affiliate_fee',
            'affiliate_fee_type',
            'customer',
            'affiliates',
            'image',
            'description',
            'headline'
        )


"""
Affiliate Schema
"""
class AffiliateSchema(Schema):
    product = fields.Nested(ProductSchema)
    customer = fields.Nested(CustomerSchema)
    class Meta:
        fields = ('id', 'product', 'customer')