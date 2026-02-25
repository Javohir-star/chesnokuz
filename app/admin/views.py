from starlette_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    fields = [
        "id",
        "email",
        "password_hash",
        "first_name",
        "last_name",
        "profession_id",
        "bio",
        "posts_count",
        "posts_read_count",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_deleted",
        "deleted_email",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = [
        "password_hash",
        "bio",
        "posts_count",
        "posts_read_count",
        "is_deleted",
        "deleted_email",
    ]
    exclude_fields_from_detail = []
    exclude_fields_from_create = [
        "id",
        "created_at",
        "updated_at",
        "posts_count",
        "posts_read_count",
    ]
    exclude_fields_from_edit = ["id", "password_hash", "created_at", "updated_at"]


class PostAdminView(ModelView):
    field = [
        "id",
        "user_id",
        "title",
        "slug",
        "body",
        "category_id",
        "views_count",
        "likes_count",
        "comments_count",
        "mins_read",
        "is_active",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = [
        "body",
        "slug",
        "views_count",
        "likes_count",
        "comments_count",
        "mins_read",
        "created_at",
        "updated_at"
    ]
    exclude_fields_from_detail = []
    exclude_fields_from_create = [
        "id",
        "created_at",
        "updated_at",
        "views_count",
        "likes_count",
        "comments_count",
        "mins_read",
    ]
    exclude_fields_from_edit = [
        "id",
        "created_at",
        "updated_at",
        "views_count",
        "likes_count",
        "comments_count",
        "mins_read",
    ]


class CategoryAdminView(ModelView):
    field = [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = ["created_at", "updated_at"]
    exclude_fields_from_detail = []
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class TagAdminView(ModelView):
    field = [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = ["created_at", "updated_at"]
    exclude_fields_from_detail = []
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class ProfessionAdminView(ModelView):
    field = [
        "id",
        "name",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = ["created_at", "updated_at"]
    exclude_fields_from_detail = []
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class MediaAdminView(ModelView):
    field = [
        "id",
        "url",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = ["created_at", "updated_at"]
    exclude_fields_from_detail = []
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class CommentAdminView(ModelView):
    field = [
        "id",
        "post_id",
        "user_id",
        "text",
        "is_active",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list = ["created_at", "updated_at"]
    exclude_fields_from_detail = []
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]