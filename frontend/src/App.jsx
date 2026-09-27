import { useState } from "react";

import Header from "./components/Header";
import ProductForm from "./components/ProductForm";
import DescriptionResult from "./components/DescriptionResult";

import "./App.css";

function App() {
  const [description, setDescription] = useState("");
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
            onDescriptionGenerated={setDescription}
            onLoading={setLoading}
            onError={setError}
          />

          <DescriptionResult
            description={description}
            loading={loading}
            error={error}
          />
        </section>
      </main>
    </div>
  );
}

export default App;