import { useState } from "react";

import Header from "./components/Header";
import ProductForm from "./components/ProductForm";
import DescriptionResult from "./components/DescriptionResult";

import "./App.css";

function App() {
  const [description, setDescription] = useState("");
  const [productName, setProductName] = useState("");
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  return (
    <div className="app">
      <Header />

      <main className="main-content">
        <section className="hero">
          <span className="hero-badge">
            AI-POWERED PRODUCT COPY
          </span>

          <h2>AI-Powered Product Descriptions</h2>

          <p>
            Give us your product details and let AI create a
            polished, customer-ready description in seconds.
          </p>
        </section>

        <section className="workspace">
          <ProductForm
            productName={productName}
            onProductNameChange={setProductName}
            onDescriptionGenerated={(result) => {
              setDescription(result.description);
              setProducts(result.products || []);
            }}
            onLoading={setLoading}
            onError={setError}
          />

          <DescriptionResult
            productName={productName}
            description={description}
            products={products}
            loading={loading}
            error={error}
          />
        </section>
      </main>
    </div>
  );
}

export default App;