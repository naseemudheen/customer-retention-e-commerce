# E-commerce Churn Detection API

![Logo](https://yourlogo.url/logo.png)

## Overview
The E-commerce Churn Detection API leverages cutting-edge machine learning algorithms to predict customer churn, helping e-commerce businesses retain their customers and enhance engagement. This tool is designed to be integrated seamlessly into any e-commerce platform, providing real-time insights and actionable data.

## Features
- **Predictive Analytics**: Accurately predicts the likelihood of customer churn.
- **Real-Time Insights**: Provides real-time predictions and risk assessments.
- **Scalable**: Supports both single and bulk predictions.
- **Easy Integration**: Simple RESTful API that integrates with any e-commerce platform.

## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- pandas
- scikit-learn
- Django REST framework

### Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ecommerce-churn-detection.git
    cd ecommerce-churn-detection
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations and start the development server:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

### API Endpoints

#### Single Prediction
- **Endpoint**: `POST /api/predict/`
- **Authorization**: `Token <your-api-token>`
- **Request Body**:
    ```json
    {
        "customer_id": "50001",
        "tenure": 18.0,
        "preferred_login_device": "Mobile",
        "city_tier": 1,
        "warehouse_to_home": 6.0,
        "preferred_payment_mode": "Debit Card",
        "gender": "Female",
        "hour_spent_on_app": 9.0,
        "number_of_device_registered": 8,
        "prefered_order_cat": "Laptop & Accessory",
        "satisfaction_score": 2,
        "marital_status": "Single",
        "number_of_address": 19,
        "complain": 0,
        "order_amount_hike_from_last_year": 11.0,
        "coupon_used": 0.0,
        "order_count": 9.0,
        "day_since_last_order": 1.0,
        "cashback_amount": 2500
    }
    ```

#### Bulk Prediction
- **Endpoint**: `POST /api/predict-multiple/`
- **Authorization**: `Token <your-api-token>`
- **Request Body**:
    ```json
    [
        {
            "customer_id": "50001",
            ...
        },
        {
            "customer_id": "50002",
            ...
        }
    ]
    ```

### Example Usage
1. Make a POST request to `/api/predict/` with the required customer data.
2. Receive a JSON response with the predicted churn risk and probability.

## Contributing
We welcome contributions to enhance the E-commerce Churn Detection API. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For enterprise solutions or support, please contact us at [support@yourcompany.com](mailto:support@yourcompany.com).

---

Thank you for using the E-commerce Churn Detection API! We hope it helps you retain your valuable customers and grow your business.
