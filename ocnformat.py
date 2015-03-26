# -*- coding: UTF-8 -*-

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

table_cat = table_db + '_cat'

columns_cat = (
    ('OFFERING_ID', 'int'),
    ('PRICE', 'int'),
    ('RENTAL_DURATION', 'int'),
    ('EXPIRATION_DATE', 'datetime'),
    ('CREATE_TIME', 'datetime'),
    ('MODIFIED_TIME', 'datetime'),
    ('SERVICE_NAME', ('varchar', 64)),
    ('SERVICE_CODE', 'int'),
    ('PACKAGE_NAME', ('char', 20)),

    ('DESCRIPTION', 'text'),

    ('TITLE_ASSET_NAME', ('varchar', 64)),
    ('MOVIE_ASSET_NAME', ('varchar', 64)),
    ('MOVIE_TITLE', ('varchar', 256)),
    ('MOVIE_RATING', ('varchar', 64)),
    ('MOVIE_RUN_TIME', 'int'),
    ('POSTER_ASSET_NAME', ('varchar', 64)),

    ('TITLE_AMS::Asset_Class', ('varchar', 64)),
    ('TITLE_AMS::Asset_ID', ('char', 20)),
    ('TITLE_AMS::Asset_Name', ('varchar', 64)),
    ('TITLE_AMS::Creation_Date', 'datetime'),
    ('TITLE_AMS::Description', ('varchar', 256)),
    ('TITLE_AMS::Product', ('varchar', 64)),
    ('TITLE_AMS::Provider', ('varchar', 64)),
    ('TITLE_AMS::Provider_ID', 'int'),
    ('TITLE_AMS::Version_Major', 'int'),
    ('TITLE_AMS::Version_Minor', 'int'),
    ('TITLE_MOD::Actors', ('varchar', 64)),
    ('TITLE_MOD::Billing_ID', 'int'),
    ('TITLE_MOD::Category', ('varchar', 64)),
    ('TITLE_MOD::Director', ('varchar', 64)),
    ('TITLE_MOD::Display_Run_Time', 'time'),
    ('TITLE_MOD::Episode_ID', 'int'),
    ('TITLE_MOD::Episode_Name', ('varchar', 64)),
    ('TITLE_MOD::Genre', ('varchar', 64)),
    ('TITLE_MOD::Licensing_Window_End', 'date'),
    ('TITLE_MOD::Licensing_Window_Start', 'date'),
    ('TITLE_MOD::Maximum_Viewing_Length', 'time'),
    ('TITLE_MOD::Preview_Period', 'int'),
    ('TITLE_MOD::Producers', ('varchar', 64)),
    ('TITLE_MOD::Provider', ('varchar', 64)),
    ('TITLE_MOD::Provider_QA_Contact', ('varchar', 64)),
    ('TITLE_MOD::Rating', ('varchar', 64)),
    ('TITLE_MOD::Run_time', 'time'),
    ('TITLE_MOD::Suggested_Price', 'float'),
    ('TITLE_MOD::Summary_Medium', 'text'),
    ('TITLE_MOD::Summary_Short', ('varchar', 256)),
    ('TITLE_MOD::Title', ('varchar', 256)),
    ('TITLE_MOD::Title_Brief', ('varchar', 64)),
    ('TITLE_MOD::Type', ('varchar', 64)),

    ('MOVIE_AMS::Asset_Class', ('varchar', 64)),
    ('MOVIE_AMS::Asset_ID', ('char', 20)),
    ('MOVIE_AMS::Asset_Name', ('varchar', 64)),
    ('MOVIE_AMS::Creation_Date', 'datetime'),
    ('MOVIE_AMS::Description', ('varchar', 256)),
    ('MOVIE_AMS::Product', ('varchar', 64)),
    ('MOVIE_AMS::Provider', ('varchar', 64)),
    ('MOVIE_AMS::Provider_ID', 'int'),
    ('MOVIE_AMS::Version_Major', 'int'),
    ('MOVIE_AMS::Version_Minor', 'int'),
    ('MOVIE_MOD::Audio_Type', ('varchar', 64)),
    ('MOVIE_MOD::Content_Checksum', ('char', 32)),
    ('MOVIE_MOD::Content_Filesize', 'bigint'),
    ('MOVIE_MOD::Content_Name', ('varchar', 64)),
    ('MOVIE_MOD::Hdcontent', ('char', 1)),
    ('MOVIE_MOD::Provider', ('varchar', 64)),
    ('MOVIE_MOD::Type', ('varchar', 64)),

    ('POSTER_AMS::Asset_Class', ('varchar', 64)),
    ('POSTER_AMS::Asset_ID', ('char', 20)),
    ('POSTER_AMS::Asset_Name', ('varchar', 64)),
    ('POSTER_AMS::Creation_Date', 'datetime'),
    ('POSTER_AMS::Description', ('varchar', 256)),
    ('POSTER_AMS::Product', ('varchar', 64)),
    ('POSTER_AMS::Provider', ('varchar', 64)),
    ('POSTER_AMS::Provider_ID', 'int'),
    ('POSTER_AMS::Version_Major', 'int'),
    ('POSTER_AMS::Version_Minor', 'int'),
    ('POSTER_MOD::Content_Checksum', ('char', 32)),
    ('POSTER_MOD::Content_Filesize', 'bigint'),
    ('POSTER_MOD::Provider', ('varchar', 64)),
    ('POSTER_MOD::Type', ('varchar', 64)),
)

primaries_cat = (
    'PACKAGE_NAME',
)

map_cat = {
    'offeringId': 'OFFERING_ID',
    'price': 'PRICE',
    'rentalDuration': 'RENTAL_DURATION',
    'expirationDate': 'EXPIRATION_DATE',
    'createTime': 'CREATE_TIME',
    'modifiedTime': 'MODIFIED_TIME',
    'serviceName': 'SERVICE_NAME',
    'serviceCode': 'SERVICE_CODE',
    'packageName': 'PACKAGE_NAME',

    'assetName': 'ASSET_NAME',
    'title': 'TITLE',
    'rating': 'RATING',
    'runTime': 'RUN_TIME',
}
