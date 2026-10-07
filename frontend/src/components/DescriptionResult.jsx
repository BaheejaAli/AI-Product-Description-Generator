function DescriptionResult({ productName, description, products, loading, error }) {
  return (
    <section className="result-card">
      <div className="card-heading">
        <span className="eyebrow">AI OUTPUT</span>

        <h2>Generated description</h2>

        <p>Your professional product description will appear here.</p>
      </div>

      {loading && (
        <div className="result-placeholder">
          <div className="result-icon">✦</div>

          <h3>Generating...</h3>

          <p>AI is creating your product description.</p>
        </div>
      )}

      {!loading && error && (
        <div className="result-placeholder">
          <div className="result-icon">!</div>

          <h3>Something went wrong</h3>

          <p>{error}</p>
        </div>
      )}

      {!loading && !error && !description && (
        <div className="result-placeholder">
          <div className="result-icon">✦</div>

          <h3>Ready when you are</h3>

          <p>
            Enter your product details and generate your description with AI.
          </p>
        </div>
      )}

      {!loading && !error && description && (
        <div className="result-content">
          <div className="description-section">
            <h2>{productName || "Product Description"}</h2>
            <p>{description}</p>
          </div>

          {products.length > 0 && (
            <div className="products-section">
              <h3>Relevant Products</h3>

              <div className="products-list">
                {products.map((product) => (
                  <div className="product-card" key={product.id}>
                    <h4>{product.title}</h4>

                    <p>{product.description}</p>

                    <div className="product-details">
                      <span>
                        <strong>Brand:</strong> {product.brand || "N/A"}
                      </span>

                      <span>
                        <strong>Category:</strong> {product.category}
                      </span>

                      <span>
                        <strong>Price:</strong> ${product.price}
                      </span>

                      <span>
                        <strong>Rating:</strong> {product.rating}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </section>
  );
}

export default DescriptionResult;
