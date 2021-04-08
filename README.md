# Wagtail + Graphql Test

This is an extremely crude test to get the StreamField working with Graphql (graphene)

The wagtail project is simply a vanilla `wagtail start {name}`

And then I added the blog app with `python manage.py startapp blog`

The graphql implementation is mainly based around:
https://wagtail.io/blog/getting-started-with-wagtail-and-graphql/
and
https://wagtail.io/blog/graphql-with-streamfield/

Tried several different mechanisms for creating graphql types from the StreamField. Unknown if any work, so I've left the most rudimentary one in place (it's basic, but not much to break).

**Issue**

The issue seems to be that in the resolver for the StreamField node field, the requested data is: `<StreamField[]>` (empty StreamField).

See: `api/schema.py ln 29`

**Points of Interest**

- Graphql schema: `api/schema.py`
- Config: `wagtailtest/settings/base.py`
  - Installed apps (api, blog, graphene_django)
  - Graphene config (line 171)

## Install

1. Clone the repo
2. Install requirements from requirements.txt
3. Make migrations
4. Migrate
5. Create super user
6. Start server
7. Add a BlogPage with some sample data via the admin
