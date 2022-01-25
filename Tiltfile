k8s_yaml('kube/rng-svc-deploy.yml')
k8s_yaml('kube/rng-svc-svc.yml')
k8s_yaml('kube/webapp-deploy.yml')
k8s_yaml('kube/webapp-svc.yml')


docker_build('danielderepentigny/webapp', 'webapp')
docker_build('danielderepentigny/rng-svc', 'rng-svc')
