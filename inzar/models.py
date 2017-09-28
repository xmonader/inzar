from enum import Enum
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listen
import string
import random


db = SQLAlchemy()  # init later in app.py
db.session.autocommit = True


class AdminLinksMixin:
    ADMIN_EDIT_LINK = "/{modelname}/edit/?id={modelid}"
    #&url=/{modelname}/"
    ADMIN_LIST_LINK = "/{modelname}/"
    # &url=/{modelname}/"
    ADMIN_VIEW_LINK = "/{modelname}/details/?id={modelid}"
    ADMIN_CREATE_LINK = "/{modelname}/new/?id={modelid}"  # &url=/{modelname}/"

    ADMIN_EDIT_LINK_MODAL = "/{modelname}/edit/?id={modelid}"  # &modal=True"
    # &modal=True"
    ADMIN_VIEW_LINK_MODAL = "/{modelname}/details/?id={modelid}"
    ADMIN_CREATE_LINK_MODAL = "/{modelname}/new/?url=/{modelname}"

    def admin_list_link(self):
        modelname = self.__class__.__name__.lower()
        return AdminLinksMixin.ADMIN_LIST_LINK.format(modelname=modelname)

    def admin_edit_link(self):
        modelname = self.__class__.__name__.lower()
        return AdminLinksMixin.ADMIN_EDIT_LINK.format(modelname=modelname, modelid=self.id)

    def admin_view_link(self):
        modelname = self.__class__.__name__.lower()

        return AdminLinksMixin.ADMIN_VIEW_LINK.format(modelname=modelname, modelid=self.id)

    def admin_create_link(self):
        modelname = self.__class__.__name__.lower()

        return AdminLinksMixin.ADMIN_CREATE_LINK.format(modelname=modelname, modelid=self.id)

    def admin_edit_link_modal(self):
        modelname = self.__class__.__name__.lower()
        return AdminLinksMixin.ADMIN_EDIT_LINK_MODAL.format(modelname=modelname, modelid=self.id)

    def admin_view_link_modal(self):
        modelname = self.__class__.__name__.lower()
        return AdminLinksMixin.ADMIN_VIEW_LINK_MODAL.format(modelname=modelname, modelid=self.id)

    def admin_create_link_modal(self):
        modelname = self.__class__.__name__.lower()

        return AdminLinksMixin.ADMIN_CREATE_LINK_MODAL.format(modelname=modelname, modelid=self.id)


class Base(AdminLinksMixin):

    id = db.Column(db.String(5), primary_key=True)
    # timestamps
    created_at = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)    
