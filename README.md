# Geospatioal imaging for crop suitability

## Objectives
* Identify and visualize regions best suited for specific crops based on weather history, soil texture, and land conditions
* Create predictive models to estimate crop suitability using long-term weather patterns and degradation indicators
* Deploy a web app and chatbot that gives planting recommendations suited to a user's location
  
## About this project:
This project helps farmers and planners in Kenya decide which crops to grow and where to plant them. It uses satellite images and soil data from the Kenya Space Agency to find the best areas for farming. The tool looks at things like how healthy the land is (using NDVI), what kind of soil is there, and weather history to give smart recommendations.

## Impact
Our model assists farmers and decision-makers with key information, making agricultural planning more resilient to climate shifts,soil and weather history.

## Stakeholders

| Stakeholder Group                   | Role / Benefit                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| **Farmers**                         | Receive data-driven recommendations to improve yield and reduce crop failure   |
| **Agricultural Extension Officers** | Use suitability maps to advise farmers more effectively on land use            |
| **Kenya Ministry of Agriculture**   | Inform national policy and resource allocation for climate-resilient farming   |
| **NGOs / Donors in Food Security**  | Target investments and interventions in regions with agricultural potential    |
| **AgriTech Developers**             | Integrate models into digital tools, mobile apps, and decision support systems |
| **Researchers & Data Scientists**   | Build upon the modeling pipeline for regional crop modeling or forecasting     |

---

#  Modeling

## Crop Suitability Prediction in Kenya Using Long-Term Environmental Data

### Overview

This modeling pipeline classifies areas in Kenya as **suitable** or **unsuitable** for crop cultivation using geospatial and environmental features. The objective is to support **climate-smart agriculture** and optimized land use planning through data-driven recommendations

---

## Objectives

- Build a supervised learning model to classify pixel regions as **suitable (1)** or **unsuitable (0)** for selected crops
- Combine long-term environmental indicators (NDVI, soil texture, soil degradation, simulated rainfall and pH) with agronomic thresholds
- Evaluate models using the **F1 Score** prioritizing balanced performance due to class imbalance

---

##  Datasets

| Dataset                              | Description                                                      |
|--------------------------------------|------------------------------------------------------------------|
| `Kenya_CropType_EndOfSeason_LongRains_2021.tiff` | Crop type raster used to generate suitability labels            |
| `Kenya NDVI 2022.tiff`               | Vegetation index (proxy for land productivity)                  |
| `Kenya Soil Degradation Data.tiff`   | Soil degradation classification                                 |
| `Kenya Soil Texture Types.tiff`      | Soil texture categories                                         |
| `crop_conditions.csv`                | Crop-specific agronomic requirements (rainfall, pH, soil type)  |

---

## Feature Engineering

- Extracted raster features per pixel across Kenya  
- Simulated rainfall and pH values to mimic realistic environmental conditions  
- Generated binary labels: `1 = Suitable`, `0 = Unsuitable`  
- Addressed class imbalance using  class weights  
- Encoded categorical variables and handled missing values  

---

## Models Tested

| Model                  | Description |
|------------------------|-------------|
| **Random Forest** | Bagged ensemble of decision trees. Performed well but had slightly lower precision |
| **XGBoost**        | Gradient boosting with regularization. **Best overall performer** by F1 score |
| **CNN**     | Convolutional neural network on NDVI patches. Limited by tiny dataset and imbalance |

---

## Evaluation

### Primary Metric: **F1 Score (Class 1: Suitable)**

**F1 Score** was chosen due to:

- Its ability to balance **precision** and **recall**
- Robustness to **class imbalance**
- Relevance to real-world agricultural impact  since missing suitable land is costlier
  
| Model             | Accuracy | F1 Score (Suitable) | Recall (Suitable) | Precision (Suitable) | Notes                                                |
|------------------|----------|---------------------|-------------------|-----------------------|------------------------------------------------------|
| **XGBoost**       | 0.90     | **0.89**            | 0.88              | 0.90                  | 🏆 Best performer; strong balance of precision & recall |
| Random Forest     | 0.85     | 0.85                | 0.90              | 0.80                  | Slightly lower precision than XGBoost                |
| CNN (Experimental)| 0.82     | 0.83                | 0.77              | 0.91                  | Small test size (N=22); unstable but promising       |


---

## Key Insights

- **XGBoost** outperformed other models in terms of F1 score and offered a strong balance between precision and recall


  <img width="380" height="278" alt="image" src="https://github.com/user-attachments/assets/1e193a9d-881e-4500-b1a1-06857aacb2d7" />

- **Random Forest** was a strong baseline but slightly less balanced
- **CNN** showed potential for spatial learning but was limited by data size and class imbalance
- **Simulated rainfall and pH** along with **soil texture** were key features influencing suitability

---
##  Conclusion

This project demonstrates the effectiveness of machine learning in classifying crop-suitable areas based on long-term environmental indicators  
The **Tuned XGBoost model** was the most reliable, offering:

- High performance in predicting suitability  
- Balanced precision and recall  
- Alignment with project objectives for **climate-resilient**, data-driven agricultural planning in Kenya  

The XGBoost classifier is ideal for real-world use by:

- Farmers deciding what to grow  
- Planners making land allocation decisions  
- Researchers building next-gen geospatial models 

Hence it's the top candidate for **real-world deployment** to assist farmers, policymakers and agricultural investors

This pipeline lays a scalable foundation for AI-powered agricultural intelligence in Kenya and beyond

---

###  Limitations  
- Binary classification simplifies crop suitability, which is often a gradient  
- CNN model was  underpowered due to limited dataset size and imbalance  
- Thresholds were fixed while in real life, crops can adapt to a wider range of conditions  

---

###  Recommendations  
- Expand to multi-class classification to model suitability for different crop types  
- Validate predictions with field data and collaborate with local agronomists  
- Scale the CNN pipeline with data augmentation and more geolocated training samples

#### Deployed link to project:
https://agriculturalsuitabilityprojector.streamlit.app/

#### Powerpoint presentation:
https://docs.google.com/presentation/d/1hWk1QSoNm9zwoLlEM-xSr5jQPHJm781lHefhC7SIGrQ/edit?usp=sharing

#### Sources:
https://www.yieldgap.org/web/guest/coverage-and-data-download

http://www.earthstat.org/

https://power.larc.nasa.gov/

https://gaez.fao.org/pages/agromaps

[https://www.fao.org/home/en](https://www.fao.org/faostat/en/#data)


