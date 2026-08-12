(= (hide $value) (empty))

!(let $import-embeddings (import! &self ../embeddings) (empty))

!(test (property-embedding access_internet)
       (0.90 0.80 0.10))

!(test (property-embedding calculate_data)
       (0.85 0.90 0.20))

!(test (property-embedding carrying_groceries)
       (0.15 0.30 0.80))
