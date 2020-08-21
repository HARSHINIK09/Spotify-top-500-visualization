from flask import Flask, request, jsonify
from flask import render_template

import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.manifold import MDS
import numpy as np
import json

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/elbowPointLocate")
def elbowPointLocate():
                global data
                localdata=data
                dictionaryvalues = {}
                elbowPoint=[]
                for k in range(1, 20):
                    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(localdata)
                    localdata["labeldata"] = kmeans.labels_
                    dictionaryvalues[k] = kmeans.inertia_
                    elbowPoint.append((k,kmeans.inertia_))
                findElbow=[]
                createElbow = pd.DataFrame(elbowPoint, columns=["x","y"])
                kn = KneeLocator(createElbow.x, createElbow.y, curve='convex', direction='decreasing')
                print("*****************ELBOW KNEE VALUE*********************")
                print(kn.knee)
                print("**********************************************")
                findElbow=pd.DataFrame(data=findElbow,columns=["x","y"])
                findElbow["x"]=list(dictionaryvalues.keys())
                findElbow["y"]=list(dictionaryvalues.values())
                findElbow = findElbow.to_dict(orient='records')
                findElbow = {'data': findElbow}
                return jsonify(findElbow)
@app.route("/createPlotScree")
def createPlotScree():
                global data               
                localdata=data
                col_names=list(localdata.columns.values)                
                df_normalized = pd.DataFrame(StandardScaler().fit_transform(localdata),columns=['danceability', 'energy', 'key note', 'loudness (dB)', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo (BPM)' , 'duration (s)'])
                pcaComponents = PCA(n_components=10)  
                pcaComponents.fit_transform(df_normalized)  
                plotValues=[]
                pdf = pd.DataFrame(data=(pcaComponents.components_),columns=col_names, index=['PCA1', 'PCA2', 'PCA3','PCA4', 'PCA5', 'PCA6','PCA7', 'PCA8', 'PCA9', 'PCA10'])
                varr = []
                for index, val in enumerate(pcaComponents.explained_variance_):
                    varr.append(val)
                pdf = pdf.T
                pdf['Sum Of Squared Loadings'] = pdf.apply(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2, axis=1)
                print('****************************************PDF*********************************************')
                print(pdf)
                print('****************************************************************************************')
                d = dict()
                for col, val in zip(df_normalized.columns.values, pdf['Sum Of Squared Loadings'].tolist()):
                    d[col] = val
                print('****************** Top 3 Attributes with highest PCA Loadings are***********************')
                print(sorted(d, key=d.get, reverse=True)[:3])
                print(f'****************************************************************************************')
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=list(pcaComponents.explained_variance_)
                plotValues = plotValues.to_dict(orient='records')
                plotValues = {'data': plotValues}
                return jsonify(plotValues)
app.route("/generateScreePlotForPCA")
def generateScreePlotForPCA():
                global data
                localdata=data
                
                global samplingdata
                localsamplingdata=samplingdata
                scaled_data = StandardScaler().fit_transform(localsamplingdata)   
                pcaComponents = PCA(n_components=10)  
                pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                plotValues=[]
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y"])
                plotValues["x"]=list(range(1,11))
         
                plotValues["y"]=list(np.cumsum(pcaComponents.explained_variance_))
                plotValues = plotValues.to_dict(orient='records')
                plotValues = {'data': plotValues}
                print(plotValues)
                return jsonify(plotValues)


@app.route("/drawScreeIntrinsic")
def drawScreeIntrinsic():
                global data
                
                localdata=data
                global samplingdata
                localsamplingdata=samplingdata
                scaled_data = StandardScaler().fit_transform(localsamplingdata)
                df_normalized = pd.DataFrame(StandardScaler().fit_transform(localdata),columns=['danceability', 'energy', 'key note', 'loudness (dB)', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo (BPM)' , 'duration (s)','clusters'])
                col_names=data.columns.values
                pcaComponents = PCA(n_components=10)  
                pcaComponents.fit_transform(df_normalized)  
                plotValues=[]

                pdf = pd.DataFrame(data=(pcaComponents.components_),columns=col_names, index=['PCA1', 'PCA2', 'PCA3','PCA4', 'PCA5', 'PCA6','PCA7', 'PCA8', 'PCA9', 'PCA10'])
                
                varr = []
                for index, val in enumerate(pcaComponents.explained_variance_):
                    varr.append(val)

                pdf = pdf.T
                pdf['Sum Of Squared Loadings'] = pdf.apply(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2, axis=1)

                print('****************************************PDF*********************************************')

                print(pdf)

                print('****************************************************************************************')

                d = dict()
                for col, val in zip(df_normalized.columns.values, pdf['Sum Of Squared Loadings'].tolist()):
                    d[col] = val
                print('****************** Top 3 Attributes with highest PCA Loadings are***********************')
                print(sorted(d, key=d.get, reverse=True)[:3])
                print(f'****************************************************************************************')
   
                pcaComponents = PCA(n_components=10)  
                pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                plotValues=[]
              
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y","z"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=list(np.cumsum(pcaComponents.explained_variance_))
                plotValues["z"]=list(pcaComponents.explained_variance_)

                plotValues = plotValues.to_dict(orient='records')

                plotValues = {'data': plotValues}
                return jsonify(plotValues)
@app.route("/drawScreeOriginal")
def drawScreeOriginal():
                global data
                
                localdata=data
                
                scaled_data = StandardScaler().fit_transform(localdata)  
                pcaComponents = PCA(n_components=10)  
                pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                plotValues=[]
               
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y","z"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=list(np.cumsum(pcaComponents.explained_variance_))
                plotValues["z"]=list(pcaComponents.explained_variance_)

                plotValues = plotValues.to_dict(orient='records')
                
                plotValues = {'data': plotValues}
                return jsonify(plotValues)




@app.route("/drawScreePCAStratified")
def drawScreePCAStratified():
                global data
                localdata=data
                col_names=list(localdata.columns.values)
                
                global stratified_sample
                stratified_sampled_data = stratified_sample
                    
                stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                scaled_data = StandardScaler().fit_transform(stratified_sampled_data)   
                pcaComponents = PCA(n_components=10)  
                components = pcaComponents.fit_transform(scaled_data)  
                plotValues=[]
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y","z"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=list(np.cumsum(pcaComponents.explained_variance_))
                plotValues["z"]=list(pcaComponents.explained_variance_)

                plotValues = plotValues.to_dict(orient='records')

                plotValues = {'data': plotValues}
                return jsonify(plotValues)
                
@app.route("/generateScreePlotForPCAStratified")
def generateScreePlotForPCAStratified():
                global data
                col_names=list(data.columns.values)
                
                global stratified_sample
                stratified_sampled_data = stratified_sample
                    
                stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                scaled_data = StandardScaler().fit_transform(stratified_sampled_data)  
                pcaComponents = PCA(n_components=10)  
                components = pcaComponents.fit_transform(scaled_data) 
                plotValues=[]
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=list(pcaComponents.explained_variance_ratio_)
                plotValues = plotValues.to_dict(orient='records')
                plotValues = {'data': plotValues}


                print("***********************")
                print(list(data.columns.values))
                print("Len",len(pcaComponents.components_))
                print(pcaComponents.components_)
                pdf = pd.DataFrame(data=(pcaComponents.components_),columns=col_names, index=['PCA1', 'PCA2', 'PCA3','PCA4', 'PCA5', 'PCA6','PCA7', 'PCA8', 'PCA9', 'PCA10'])
                
                varr = []
                for index, val in enumerate(pcaComponents.explained_variance_):
                    varr.append(val)

                pdf = pdf.T



                pdf['Sum Of Squared Loadings'] = pdf.apply(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2, axis=1)
                print()
                print('****************************************************************************************')
                print()
                print(pdf)
                print()
                print('****************************************************************************************')
                print()
                d = dict()
                for col, val in zip(stratified_sampled_data.columns.values, pdf['Sum Of Squared Loadings'].tolist()):
                    d[col] = val
                print('****************** Top 3 Attributes with highest PCA Loadings are***********************')
                print(sorted(d, key=d.get, reverse=True)[:3])
                print(f'****************************************************************************************')



                
                return jsonify(plotValues)

@app.route("/generateScreePlotForMDSEuc")
def generateScreePlotForMDSEuc():
                global data
                global samplingdata
                localsamplingdata=samplingdata
                scaled_data=StandardScaler().fit_transform(localsamplingdata)
                stress=[]

                print("********MDS EUC SCREE")
                for m in range(1,11):
                    euclidean_mds = MDS(n_components=m, dissimilarity='euclidean')
                    euclidean_mds.fit_transform(scaled_data)
                    stress.append(euclidean_mds.stress_)
                plotValues=[]
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=stress
                plotValues = plotValues.to_dict(orient='records')
                plotValues = {'data': plotValues}
                return jsonify(plotValues)

@app.route("/drawScatterOriginal")
def drawScatterOriginal():
                global data
                global samplingdata
                
                localdata=data
                scaled_data = StandardScaler().fit_transform(localdata)   
                pcaComponents = PCA(n_components=2)  
                pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                scatter_plt_data = pd.DataFrame(data=pcaComponents_data,columns=['x', 'y'])
                scatter_plt_data = scatter_plt_data.to_dict(orient='records')
                scatter_plt_data = {'data': scatter_plt_data}
                return jsonify(scatter_plt_data)




@app.route("/generateScreePlotForMDSEucStratified")
def generateScreePlotForMDSEucStratified():
                global data
                
                global stratified_sample
                stratified_sampled_data = stratified_sample
                    
                stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                scaled_data = StandardScaler().fit_transform(stratified_sampled_data)   
                stress=[]
                for m in range(1,11):
                    euclidean_mds = MDS(n_components=m, dissimilarity='euclidean')
                    euclidean_mds.fit_transform(scaled_data)
                    stress.append(euclidean_mds.stress_)
                plotValues=[]
                plotValues=pd.DataFrame(data=plotValues,columns=["x","y"])
                plotValues["x"]=list(range(1,11))
                plotValues["y"]=stress
                plotValues = plotValues.to_dict(orient='records')
                plotValues = {'data': plotValues}
                return jsonify(plotValues)


@app.route("/ScatterPlotPCA")
def ScatterPlotPCA():
                global data
                
                global samplingdata
                print("******************PCA SCATTER")
                localsamplingdata=samplingdata
                scaled_data = StandardScaler().fit_transform(localsamplingdata)  
                pcaComponents = PCA(n_components=2)  
                pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                scatter_plt_data = pd.DataFrame(data=pcaComponents_data,columns=['x', 'y'])
                scatter_plt_data = scatter_plt_data.to_dict(orient='records')
                scatter_plt_data = {'data': scatter_plt_data}
                return jsonify(scatter_plt_data)


@app.route("/ScatterPlotPCAStratified")
def ScatterPlotPCAStratified():
                    global data
                   
                    global stratified_sample
                    stratified_sampled_data = stratified_sample
                    
                    clusters_columns=stratified_sampled_data["clusters"]
                    stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                    scaled_data = StandardScaler().fit_transform(stratified_sampled_data)   
                    pcaComponents = PCA(n_components=2) 
                    pcaComponents_data = pcaComponents.fit_transform(scaled_data)  
                    pcaComponents_data=np.append(pcaComponents_data,clusters_columns.values.reshape(len(pcaComponents_data),1),axis=1)
                    scatter_plt_data = pd.DataFrame(data=pcaComponents_data,columns=['x', 'y','cluster'])
                    scatter_plt_data = scatter_plt_data.to_dict(orient='records')
                    scatter_plt_data = {'data': scatter_plt_data}
                    return jsonify(scatter_plt_data)


@app.route("/ScatterPlotMDS")
def ScatterPlotMDS():
                    global data
                    
                    global samplingdata
                    
                    localsamplingdata=samplingdata
                    scaled_data=StandardScaler().fit_transform(localsamplingdata)
                    euclidean_mds = MDS(n_components=2, dissimilarity='euclidean')
                    euclidean_mds_data = pd.DataFrame(data=euclidean_mds.fit_transform(scaled_data),columns=['x', 'y'])
                    euclidean_mds_data = euclidean_mds_data.to_dict(orient='records')
                    euclidean_mds_data = {'data': euclidean_mds_data}
                    return jsonify(euclidean_mds_data)
@app.route("/drawMDSOriginal")
def drawMDSOriginal():
                    global data
                    
                    global samplingdata
                   
                    localdata=data
                    scaled_data=StandardScaler().fit_transform(localdata)
                    euclidean_mds = MDS(n_components=2, dissimilarity='euclidean')
                    euclidean_mds_data = pd.DataFrame(data=euclidean_mds.fit_transform(scaled_data),columns=['x', 'y'])
                    euclidean_mds_data = euclidean_mds_data.to_dict(orient='records')
                    euclidean_mds_data = {'data': euclidean_mds_data}
                    return jsonify(euclidean_mds_data)




@app.route("/ScatterPlotMDSStratified")
def ScatterPlotMDSStratified():
                    global data
                    
                    global stratified_sample
                    stratified_sampled_data = stratified_sample
                    
                    clusters_columns=stratified_sampled_data["clusters"]
                    stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                    scaled_data = StandardScaler().fit_transform(stratified_sampled_data)   
                    euclidean_mds = MDS(n_components=2, dissimilarity='euclidean')
                    euclidean_mds_data = euclidean_mds.fit_transform(scaled_data)  
                    euclidean_mds_data=np.append(euclidean_mds_data,clusters_columns.values.reshape(len(euclidean_mds_data),1),axis=1)
                    scatter_plt_data = pd.DataFrame(data=euclidean_mds_data,columns=['x', 'y','cluster'])
                    scatter_plt_data = scatter_plt_data.to_dict(orient='records')
                    scatter_plt_data = {'data': scatter_plt_data}
                    return jsonify(scatter_plt_data)

@app.route("/drawMDSCorrOriginal")
def drawMDSCorrOriginal():
                    global data
                   
                    global samplingdata
                    
                    localdata=data
                    scaled_data=StandardScaler().fit_transform(localdata)
                    dis_mat = metrics.pairwise_distances(scaled_data, metric='correlation')
                    correlation_mds = MDS(n_components=2, dissimilarity='precomputed')
                    correlation_mds_data = correlation_mds.fit_transform(dis_mat)
                    correlation_mds_data = pd.DataFrame(data=correlation_mds_data,columns=['x', 'y'])
                    correlation_mds_data = correlation_mds_data.to_dict(orient='records')
                    correlation_mds_data = {'data': correlation_mds_data}
                    return jsonify(correlation_mds_data)



@app.route("/ScatterPlotMDSCorr")
def ScatterPlotMDSCorr():
                    global data
   
                    global samplingdata
                    
                    localsamplingdata=samplingdata
                    scaled_data=StandardScaler().fit_transform(localsamplingdata)
                    dis_mat = metrics.pairwise_distances(scaled_data, metric='correlation')
                    correlation_mds = MDS(n_components=2, dissimilarity='precomputed')
                    correlation_mds_data = correlation_mds.fit_transform(dis_mat)
                    correlation_mds_data = pd.DataFrame(data=correlation_mds_data,columns=['x', 'y'])
                    correlation_mds_data = correlation_mds_data.to_dict(orient='records')
                    correlation_mds_data = {'data': correlation_mds_data}
                    return jsonify(correlation_mds_data)

@app.route("/ScatterPlotMDSCorrStratified")
def ScatterPlotMDSCorrStratified():
                    global data
                    
                    global stratified_sample
                    stratified_sampled_data = stratified_sample
                    clusters_columns=stratified_sampled_data["clusters"]
                    stratified_sampled_data=stratified_sampled_data.drop(['clusters'], axis=1)
                    scaled_data = StandardScaler().fit_transform(stratified_sampled_data)   
                    dis_mat = metrics.pairwise_distances(scaled_data, metric='correlation')
                    correlation_mds = MDS(n_components=2, dissimilarity='precomputed')
                    correlation_mds_data = correlation_mds.fit_transform(dis_mat)  
                    
                    correlation_mds_data=np.append(correlation_mds_data,clusters_columns.values.reshape(len(correlation_mds_data),1),axis=1)
                    scatter_plt_data = pd.DataFrame(data=correlation_mds_data,columns=['x', 'y','cluster'])
                    scatter_plt_data = scatter_plt_data.to_dict(orient='records')
                    scatter_plt_data = {'data': scatter_plt_data}
                    return jsonify(scatter_plt_data)


@app.route("/originalDataMatrix")
def originalDataMatrix():
                    global data
                   
                    localdata=data
                    scaled_data = StandardScaler().fit_transform(localdata)   
                    print("******original data matrix*********")
                    print(list(data.columns.values))
                    df_normalized = pd.DataFrame(scaled_data,columns=['danceability', 'energy', 'key note', 'loudness (dB)', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo (BPM)' , 'duration (s)','clusters'])
                    print(df_normalized)
                    stratified_sampled_data=df_normalized.drop(['clusters','energy', 'key note', 'loudness (dB)','acousticness', 'instrumentalness', 'liveness', 'valence', 'duration (s)'], axis=1)
                    scatter_plt_matrix_data = stratified_sampled_data.to_dict(orient='records')
                    scatter_plt_matrix_data = {'data': scatter_plt_matrix_data}
                    
                    
                    return jsonify(scatter_plt_matrix_data)

@app.route("/RandomSamplingMatrix")
def RandomSamplingMatrix():
                    global data

                    global df_normalized
                    print("HERE IN RS MATRIX")
                    stratified_sampled_data=df_normalized.drop(['energy', 'key note', 'loudness (dB)','acousticness', 'instrumentalness', 'liveness', 'valence', 'duration (s)'], axis=1)
                    scatter_plt_matrix_data = stratified_sampled_data.to_dict(orient='records')
                    scatter_plt_matrix_data = {'data': scatter_plt_matrix_data}
                    
                    return jsonify(scatter_plt_matrix_data)

@app.route("/stratifiedScatterPlotMatrix")
def stratifiedScatterPlotMatrix():
                    global data
                    
                    global stratified_sample
                    stratified_sampled_data = stratified_sample
                    stratified_sampled_data=stratified_sampled_data.drop(['energy', 'key note', 'loudness (dB)','acousticness', 'instrumentalness', 'liveness', 'valence', 'duration (s)'], axis=1)
                    scatter_plt_matrix_data = stratified_sampled_data.to_dict(orient='records')
                    scatter_plt_matrix_data = {'data': scatter_plt_matrix_data}
                    print("*****************************************************")
                    print(scatter_plt_matrix_data)
                    return jsonify(scatter_plt_matrix_data)

if __name__ == "__main__":
    data = pd.read_csv("spotify_top_500.csv")
    stratpoints= pd.read_csv("spotify_top_500.csv")
    randompoints= pd.read_csv("spotify_top_500.csv")
    randompoints=randompoints.sample(frac=0.25)  
    samplingdata=randompoints
    knee = 6
    scaled_data = StandardScaler().fit_transform(randompoints)                  
    df_normalized = pd.DataFrame(scaled_data,columns=['danceability', 'energy', 'key note', 'loudness (dB)', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo (BPM)' , 'duration (s)'])
    #print(df_normalized)
    kmeans = KMeans(n_clusters=knee)
    kmeans = kmeans.fit(stratpoints)
    stratpoints["clusters"] = kmeans.labels_
    minimum=min(len(stratpoints[stratpoints["clusters"]==0]),len(stratpoints[stratpoints["clusters"]==1]),len(stratpoints[stratpoints["clusters"]==2]),len(stratpoints[stratpoints["clusters"]==3]))

    clustA=stratpoints[stratpoints["clusters"]==0].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==0])))
    
    clustB=stratpoints[stratpoints["clusters"]==1].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==1])))
    
    clustC=stratpoints[stratpoints["clusters"]==2].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==2])))
    
    clustD=stratpoints[stratpoints["clusters"]==3].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==3])))

    clustE=stratpoints[stratpoints["clusters"]==4].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==4])))

    clustF=stratpoints[stratpoints["clusters"]==5].sample(round(0.25*len(stratpoints[stratpoints["clusters"]==5])))
    
    stratified_sample=[]
    dfObj = pd.DataFrame(stratified_sample, columns=['danceability', 'energy', 'key note', 'loudness (dB)', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo (BPM)' , 'duration (s)', 'clusters'])
    stratified_sample=dfObj.append(clustA,ignore_index=True).append(clustB,ignore_index=True).append(clustC,ignore_index=True).append(clustD,ignore_index=True).append(clustE,ignore_index=True).append(clustF,ignore_index=True)
    app.run(host='0.0.0.0',port=5000,debug=True)
