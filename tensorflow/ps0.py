import tensorflow as tf
cluster=tf.train.ClusterSpec({
    "worker": [
        "localhost:2222",
        "localhost:2223",
    ],
    "ps": [
        "localhost:2224",
        "localhost:2225"
    ]})

server=tf.train.Server(cluster, job_name="ps",task_index=0)

    with tf.device("/job:ps/task:0"):
        W = tf.Variable(tf.zeros[784,10]))

    with tf.device("/job:ps/task:1"):
        b = tf.Variable(tf.zeros([10]))

    with tf.device("/job:worker/task:0"):
        x = tf.placeholder(tf.float32, [None, 784])
        y = tf.nn.softmax(tf.matmul(x, W) + b)
        y_ = tf.placeholder(tf.float32, [None, 10])
        


        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        init = tf.global_variables_initializer()

        sess = tf.Session()
        sess.run(init)


    with tf.device("/job:worker/task:1"):
        global_step = tf.Variable(0)
        train_op = tf.train.AdagradOptimizer(0.01).minimize(
            loss, global_step=global_step)
        saver = tf.train.Saver()
        summary_op = tf.summary.merge_all()
        init_op = tf.global_variables_initializer()
        
