from everywhereml.data import Dataset
from everywhereml.data.collect import SerialCollector

"""
Create a SerialCollector object.
Each data line is marked by the 'MPU:' string
Collect 30 seconds of data for each gesture
Replace the port with your own!

If a mpu.csv file already exists, skip collection
"""

try:
    mpu_dataset = Dataset.from_csv(
        'mpu.csv', 
        name='ContinuousMotion', 
        target_name_column='target_name'
    )
    
except FileNotFoundError:
    mpu_collector = SerialCollector(
        port='/dev/ttyUSB1', 
        baud=115200, 
        start_of_frame='MPU:', 
        feature_names=['ax', 'ay', 'az', 'gx', 'gy', 'gz']
    )
    mpu_dataset = mpu_collector.collect_many_classes(
        dataset_name='ContinuousMotion', 
        duration=30
    )
    # save dataset to file for later use
    mpu_dataset.df.to_csv('mpu.csv', index=False)





    mpu_dataset.describe()





    mpu_dataset.plot.features_pairplot(n=300)





    from everywhereml.preprocessing import Pipeline, MinMaxScaler, Window, SpectralFeatures

    # this is the frequency of your sensor
    # change according to your hardware
    sampling_frequency = 104
    mean_gesture_duration_in_millis = 1000
    window_length = sampling_frequency * mean_gesture_duration_in_millis // 1000

    mpu_pipeline = Pipeline(name='ContinousMotionPipeline', steps=[
        MinMaxScaler(),
        # shift can be an integer (number of samples) or a float (percent)
        Window(length=window_length, shift=0.3),
        # order can either be 1 (first-order features) or 2 (add second-order features)
        SpectralFeatures(order=2)
    ])





    from pprint import pprint
    pprint(mpu_pipeline['SpectralFeatures'][0].feature_names)






    mpu_dataset.apply(mpu_pipeline)





    mpu_dataset.plot.features_pairplot(n=300, k=6)





    '''Perform classification with a RandomForest'''
    from everywhereml.sklearn.ensemble import RandomForestClassifier
    mpu_classifier = RandomForestClassifier(n_estimators=20, max_depth=20)
    mpu_train, mpu_test = mpu_dataset.split(test_size=0.3)
    mpu_classifier.fit(mpu_train)
    print('Score on test set: %.2f' % mpu_classifier.score(mpu_test))





    '''Port pipeline to C++'''
    print(mpu_pipeline.to_arduino_file('sketches/MPUClassify/Pipeline.h', instance_name='pipeline'))




    '''Port classifier to C++'''
    print(mpu_classifier.to_arduino_file('sketches/MPUClassify/Classifier.h', instance_name='forest', class_map=mpu_dataset.class_map))
