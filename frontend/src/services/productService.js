const API_URL = "http://127.0.0.1:8000/api/products/generate/";

export async function generateProductDescription(productName, features) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      product_name: productName,
      features: features,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.error || "Failed to generate product description."
    );
  }

  return data.description;
}