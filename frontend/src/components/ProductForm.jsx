import { useState } from "react";
import { generateProductDescription } from "../services/productService";

function ProductForm({ onDescriptionGenerated, onLoading, onError }) {
  const [productName, setProductName] = useState("");
  const [features, setFeatures] = useState([""]);

  const handleFeatureChange = (index, value) => {
    const updatedFeatures = [...features];

    updatedFeatures[index] = value;

    setFeatures(updatedFeatures);
  };

  const addFeature = () => {
    setFeatures([...features, ""]);
  };

  const handleGenerate = async () => {
    onError("");

    const cleanedFeatures = features
      .map((feature) => feature.trim())
      .filter((feature) => feature !== "");

    if (!productName.trim()) {
      onError("Please enter a product name.");
      return;
    }

    if (cleanedFeatures.length === 0) {
      onError("Please add at least one feature.");
      return;
    }

    try {
      onLoading(true);

      const description = await generateProductDescription(
        productName.trim(),
        cleanedFeatures
      );

      onDescriptionGenerated(description);
    } catch (error) {
      onError(error.message);
    } finally {
      onLoading(false);
    }
  };

  return (
    <section className="form-card">
      <div className="card-heading">
        <span className="eyebrow">PRODUCT DETAILS</span>

        <h2>Tell us about your product</h2>

        <p>
          Add the product name and key features. AI will turn them
          into polished, customer-ready description.
        </p>
      </div>

      <div className="form-group">
        <label htmlFor="product-name">
          Product name
        </label>

        <input
          id="product-name"
          type="text"
          placeholder="e.g. Wireless Bluetooth Headphones"
          value={productName}
          onChange={(event) =>
            setProductName(event.target.value)
          }
        />
      </div>

      <div className="form-group">
        <div className="label-row">
          <label>Features</label>

          <span>
            {features.length} added
          </span>
        </div>

        <div className="feature-list">
          {features.map((feature, index) => (
            <input
              key={index}
              type="text"
              placeholder={`Feature ${index + 1}`}
              value={feature}
              onChange={(event) =>
                handleFeatureChange(
                  index,
                  event.target.value
                )
              }
            />
          ))}
        </div>

        <button
          type="button"
          className="add-feature"
          onClick={addFeature}
        >
          + Add feature
        </button>
      </div>

      <button
        type="button"
        className="generate-button"
        onClick={handleGenerate}
      >
        <span>✦</span>
        Generate with AI
      </button>
    </section>
  );
}

export default ProductForm;