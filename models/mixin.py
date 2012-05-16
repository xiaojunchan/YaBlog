# -*- coding:utf-8 -*-
"""
    @author messense
    @date 2012-05-11
    I love cici.
    I miss you.
    Can you hear me?
"""
from models import Post, Category, Tag, Link
from config import db

class PostMixin(object):

    def get_post_by_id(self, id):
        return Post.query.filter_by(id=id).first()

    def get_post_by_slug(self, slug):
        return Post.query.filter_by(slug=slug).first()

    def get_post_by_title(self, title):
        return Post.query.filter_by(title=title).first()

    def get_posts_by_category(self, id):
        return Post.query.filter_by(type=Post.TYPE_POST, category_id=id).all()

    def get_posts_by_ids(self, ids):
        return Post.query.filter_by(id__in=ids).all()

    def get_all_posts(self):
        return Post.query.filter_by(type=Post.TYPE_POST).all()

    def get_all_pages(self):
        return Post.query.filter_by(type=Post.TYPE_PAGE).all()

class CategoryMixin(object):

    def get_category_by_id(self, id):
        return Category.query.filter_by(id=id).first()

    def get_category_by_slug(self, slug):
        return Category.query.filter_by(slug=slug).first()

    def get_category_by_title(self, title):
        return Category.query.filter_by(title=title).first()

    def get_category_by_ids(self, ids):
        return Category.query.filter_by(id__in=ids).all()

    def get_all_categories(self):
        return Category.query.all()

class TagMixin(object):

    def get_tag_by_id(self, id):
        return Tag.query.filter_by(id=id).first()

    def get_tag_by_slug(self, slug):
        return Tag.query.filter_by(slug=slug).first()

    def get_tag_by_title(self, title):
        return Tag.query.filter_by(title=title).first()

    def get_all_tags(self):
        return Tag.query.all()

    def get_tags_by_ids(self, ids):
        return Tag.query.filter_by(id__in=ids).all()

    def create_tags(self, tags, post_id):
        post_tags = ''
        if tags is str:
            tags = tags.split(',')
        for tag in tags:
            the_tag = self.get_tag_by_title(tag)
            if not the_tag:
                the_tag = Tag()
                the_tag.title = tag
                the_tag.slug = tag
                the_tag.post_count = 1
            else:
                the_tag.post_count += 1
            if not the_tag.post_ids:
                the_tag.post_ids = '%s' % post_id
            else:
                ids = the_tag.post_ids.split('|').append(post_id)
                ids = list(set(ids))
                the_tag.post_ids = '|'.join(ids)
            db.session.add(the_tag)
            if post_tags == '':
                post_tags = '%s' % the_tag.id
            else:
                post_tags = '%s|%s' % (post_tags, the_tag.id)
        db.session.commit()
        return post_tags

class LinkMixin(object):

    def get_link_by_id(self, id):
        return Link.query.filter_by(id=id).first()

    def get_link_by_title(self, title):
        return Link.query.filter_by(title=title).first()

    def get_all_links(self):
        return Link.query.all()

    def get_links_by_ids(self, ids):
        return Link.query.filter_by(id__in=ids).all()