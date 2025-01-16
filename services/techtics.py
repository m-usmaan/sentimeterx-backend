import json
import os
import requests


class TechticsClient:
    def __init__(self) -> None:
        self.secret_key = str(os.getenv('TECHTICS_SECRET_KEY'))
        self.base_url = str(os.getenv('TECHTICS_API_URL'))

    @property
    def _headers(self):
        return {
            "accept": "application/json",
            "secret-key": self.secret_key
        }

    def get_chat_suggestions(self):
        url = f'{self.base_url}/get-pre-defined-questions/'
        response = requests.get(url, headers=self._headers, verify=False)
        if response.status_code == 200:
            return json.loads(response.text)

        raise Exception('An error occured')

    def get_data_sets(self):
        url = f'{self.base_url}/get-data-sources/'
        response = requests.get(url, headers=self._headers, verify=False)
        if response.status_code == 200:
            return json.loads(response.text)

        raise Exception('An error occured')

    def get_summary(self, user_query: str, chat_id: str):
        return {
            "summary": {
                "headline": "Unified sentiment shows unanimous suggestions from user feedback",
                "comparison": [
                    {
                        "score": "0",
                        "description": "Feedback demonstrates overwhelming unanimous suggestions",
                        "chart": {
                            "label_1": "Suggestion",
                            "value_1": "521 (38.00%)"
                        }
                    },
                    {
                        "score": -1,
                        "description": "65% customer mentioned that countdown starts before the parcel arrives",
                        "chart": {
                            "label_1": "Complaints Up",
                            "value_1": "36%"
                        }
                    },
                    {
                        "score": 1,
                        "description": "28% customer discussed competitors have 30 day free return window",
                        "chart": {
                            "label_1": "Issues Down",
                            "value_1": "16%"
                        }
                    }
                ]
            },
            "Comments": "521 of 2350 Records",
            "Datasets": "Customer Feedback NPS Survey"
        }
        url = f'{self.base_url}/generate-response/'
        response = requests.post(
            url, headers=self._headers, verify=False,
            data={'user_query': user_query, 'chat_id': chat_id}
        )
        if response.status_code == 200:
            return json.loads(response.text)

        raise Exception('An error occured')

    def get_visualization(self, chat_id: str):
        data = {
            "query": "What are the suggestions?",
            "chart_data": {
                "labels": [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July"
                ],
                "datasets": [
                    {
                        "label": "Monthly Sales (in USD)",
                        "data": [
                            12000,
                            15000,
                            10000,
                            18000,
                            17000,
                            22000,
                            25000
                        ]
                    },
                    {
                        "label": "Monthly Profit (in USD)",
                        "data": [
                            3000,
                            4000,
                            2000,
                            5000,
                            4500,
                            6000,
                            8000
                        ]
                    },
                    {
                        "label": "Growth Rate (%)",
                        "data": [
                            15000,
                            15000,
                            5000,
                            2000,
                            18000,
                            2500,
                            30000
                        ]
                    }
                ]
            }
        }
        return data

    def get_analysis(self, chat_id: str):
        data = {
            "query": "What are the suggestions?",
            "analysis": {
                "detail": "The feedback analysis has unequivocally indicated that all users have provided suggestions, evidenced by a total count of 521 suggestions making up 100.00% of the feedback collected. This suggests a homogenous sentiment where every single piece of feedback falls under the 'Suggestion' category. No other feedback categories have been recorded, which is highly significant as it points towards users having a very clear and uniform message or area of interest that all suggestions align with. This could simplify the decision-making process for stakeholders as there is a clear pathway defined by unanimous user input. Such a singular direction as represented by the complete 100.00% underlines a lack of division or alternative concerns within this dataset. This homogeneity suggests an area of strong agreement among users that presumably requires attention or action. Without opposing voices or alternate categories, the path to improvement or acknowledgment is distinct, as all user feedback is concentrated on making suggestions.",
                "headline": "Unified sentiment shows unanimous suggestions from user feedback"
            }
        }
        return data

    def get_feedback_quotes(self, chat_id: str):
        quotes = {
            "query": "What are the suggestions?",
            "reviews": [
                {
                    "id": 1,
                    "text": "Mostly I get second day deliveries and sometimes things ordered are not available.",
                    "timestamp": "08/03/2024",
                    "customer_id": 1785729
                },
                {
                    "id": 2,
                    "text": "Great product quality but the packaging could be improved.",
                    "timestamp": "12/01/2024",
                    "customer_id": 1785730
                },
                {
                    "id": 3,
                    "text": "Customer service was very helpful when I needed assistance with my order.",
                    "timestamp": "15/02/2024",
                    "customer_id": 1785731
                },
                {
                    "id": 4,
                    "text": "I received a damaged item, but the refund process was quick and easy.",
                    "timestamp": "20/02/2024",
                    "customer_id": 1785732
                },
                {
                    "id": 5,
                    "text": "The website is user-friendly and the checkout process is smooth.",
                    "timestamp": "25/02/2024",
                    "customer_id": 1785733
                },
                {
                    "id": 6,
                    "text": "Delivery was delayed by a week, but the product was worth the wait.",
                    "timestamp": "03/03/2024",
                    "customer_id": 1785734
                },
                {
                    "id": 7,
                    "text": "Very satisfied with the purchase. Will definitely buy again.",
                    "timestamp": "10/03/2024",
                    "customer_id": 1785735
                },
                {
                    "id": 8,
                    "text": "Item was missing from my order but resolved promptly after contact.",
                    "timestamp": "14/03/2024",
                    "customer_id": 1785736
                },
                {
                    "id": 9,
                    "text": "The variety of products available is impressive, great selection!",
                    "timestamp": "18/03/2024",
                    "customer_id": 1785737
                },
                {
                    "id": 10,
                    "text": "I love the eco-friendly packaging. Keep up the good work!",
                    "timestamp": "22/03/2024",
                    "customer_id": 1785738
                },
                {
                    "id": 11,
                    "text": "The product description was misleading, but customer support clarified my concerns.",
                    "timestamp": "25/03/2024",
                    "customer_id": 1785739
                },
                {
                    "id": 12,
                    "text": "Good experience overall, but I'd appreciate faster delivery options.",
                    "timestamp": "28/03/2024",
                    "customer_id": 1785740
                },
                {
                    "id": 13,
                    "text": "Highly recommend this store for its excellent customer service.",
                    "timestamp": "31/03/2024",
                    "customer_id": 1785741
                }
            ]
        }
        return quotes

    def get_filters(self, dataset_id: str):
        url = f'{self.base_url}/get-filters/{dataset_id}/'
        response = requests.get(url, headers=self._headers, verify=False)
        if response.status_code == 200:
            return json.loads(response.text)

        raise Exception('An error occured')
