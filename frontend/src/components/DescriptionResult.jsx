function DescriptionResult({description,loading,error}) {
  return (
    <section className="result-card">
      <div className="card-heading">
        <span className="eyebrow">AI OUTPUT</span>

        <h2>Generated description</h2>

        <p>
          Your professional product description will appear
          here.
        </p>
      </div>

      {loading && (
        <div className="result-placeholder">
          <div className="result-icon">✦</div>

          <h3>Generating...</h3>

          <p>
            AI is creating your product description.
          </p>
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
            Enter your product details and generate your
            description with AI.
          </p>
        </div>
      )}

      {!loading && !error && description && (
        <div className="result-content">
          <p>{description}</p>
        </div>
      )}
    </section>
  );
}

export default DescriptionResult;