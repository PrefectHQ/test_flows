from prefect import flow                                                       
from prefect.deployments import DeploymentImage                                
                                                                                
                                                                           
@flow(log_prints=True)                                                         
def my_flow(name: str = "world"):                                              
    print(f"Hello {name}! I'm a flow running on an Azure Container Instance!") 
                                                                                
                                                                                
if __name__ == "__main__":                                                     
    my_flow.deploy(                                                            
        name="my-deployment-with-a-very-very-very-long-name",
        work_pool_name="workercontainer",                                                  
        image=DeploymentImage(                                                 
            name="flow-image:latest",                                            
            platform="linux/amd64",                                            
        )                                                                      
    )    