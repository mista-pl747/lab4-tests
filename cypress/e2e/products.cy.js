describe('Products API', () => {
  it('creates a new product and then retrieves it', () => {
    const newProduct = {
      name: 'Test Product',
      price: 99.99
    };

    // 1. Створюємо продукт
    cy.request('POST', '/products', newProduct).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('id');
      expect(response.body.name).to.eq(newProduct.name);
      
      const productId = response.body.id;

      // 2. Отримуємо щойно створений продукт
      cy.request('GET', `/products/${productId}`).then((getResponse) => {
        expect(getResponse.status).to.eq(200);
        expect(getResponse.body.id).to.eq(productId);
        expect(getResponse.body.name).to.eq(newProduct.name);
        expect(getResponse.body.price).to.eq(newProduct.price);
      });
    });
  });

  it('returns 404 for a non-existent product', () => {
    // 3. Перевіряємо помилку 404
    cy.request({
      method: 'GET',
      url: '/products/999999', 
      failOnStatusCode: false 
    }).then((response) => {
      expect(response.status).to.eq(404);
      expect(response.body.detail).to.eq('Not found');
    });
  });
});