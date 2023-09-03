class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant
    def full_review(self):
        return f"Review for {self.restaurant.name()} by {self.customer.full_name()}: {self.star_rating} stars."
    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'star_rating={self.star_rating}, ' + \
            f'restaurant_id={self.restaurant_id}), ' +\
            f'customer_id={self.customer_id})'