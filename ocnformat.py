table_db = 'dbtest2'

columns_db = (
    ('STB_NO', ('char', 17)),
    ('SERVICE_CODE', 'int'),
    ('PROVIDER', ('varchar', 64)),
    ('ASSET_NAME', ('varchar', 64)),
    ('CONTENT_NAME', ('varchar', 64)),
    ('RENTAL_TIME', 'datetime'),
    ('RENTAL_EXPIRE_TIME', 'datetime'),  # may be unavaliable
)

primaries_db = (
    'STB_NO',
    # 'SERVICE_CODE', 'PROVIDER',
    # 'ASSET_NAME', 'CONTENT_NAME',
    'RENTAL_TIME', 'RENTAL_EXPIRE_TIME',
)
