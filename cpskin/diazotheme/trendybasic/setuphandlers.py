# -*- coding: utf-8 -*-
import os
from plone import api
IMAGESHEADER = 'images-header'


def setup_various(context):
    if context.readDataFile('cpskin.diazotheme.trendybasic.marker.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()
    if not hasattr(portal, IMAGESHEADER):
        ih_folder = api.content.create(
            type='Folder',
            title='Image header',
            id=IMAGESHEADER,
            container=portal
        )
        ih_folder.setTitle('Image header')
        ih_folder.reindexObject()
        add_images_from_file(ih_folder, 'header.jpg')
        add_images_from_file(ih_folder, 'header-t1.jpg')
        add_images_from_file(ih_folder, 'header-t2.jpg')
        add_images_from_file(ih_folder, 'header-t3.jpg')
        add_images_from_file(ih_folder, 'header-t4.jpg')


def add_images_from_file(context, filename):
    datapath = os.path.join(os.path.dirname(__file__), 'static', 'images')
    filepath = os.path.join(datapath, 'header.jpg')
    fd = open(filepath, 'rb')
    if not context.hasObject(filename):
        image = api.content.create(
            type='Image',
            title=filename,
            container=context,
            file=fd
        )
        image.setTitle(filename)
        image.reindexObject()
        fd.close()
