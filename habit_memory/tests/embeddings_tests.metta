(= (hide $value) (empty))

!(let $import-embeddings (import! &self ../embeddings) (empty))

!(test (property-embedding access_internet)
       (0.90 0.80 0.10))

!(test (property-embedding calculate_data)
       (0.85 0.90 0.20))

!(test (property-embedding carrying_groceries)
       (0.15 0.30 0.80))

!(test (dot-product (1.0 2.0 3.0) (4.0 5.0 6.0))
       32.0)

!(test (vector-norm (3.0 4.0))
       5.0)

!(test (cosine-similarity (1.0 0.0) (0.0 1.0))
       0.0)

!(test (cosine-similarity (1.0 1.0) (1.0 1.0))
       0.9999999999999998)

!(test (cosine-similarity
          (property-embedding access_internet)
          (property-embedding calculate_data))
       0.9932641140158293)
