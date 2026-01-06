def paginate(page: int = 1, size: int = 20):
    skip = (page - 1) * size
    limit = size
    return skip, limit
