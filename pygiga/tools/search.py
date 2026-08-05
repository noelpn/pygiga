"""Search tool."""

class SearchTool:
    """Performs simple text searches."""

    def search(self, query, corpus):
        return [item for item in corpus if query.lower() in item.lower()]
