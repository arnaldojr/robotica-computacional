from module_aruco import Aruco3d
from module import ImageModule
import cv2
import numpy as np

class DistanceEstimator(Aruco3d, ImageModule):
    def __init__(self):
        Aruco3d.__init__(self)
        ImageModule.__init__(self)

        # configure o kernel

        self.filters = {
            'blue': {
                'lower': np.array([0, 0, 0]),
                'upper': np.array([180, 255, 255])
            },
            'green': {
                'lower': np.array([0, 0, 0]),
                'upper': np.array([180, 255, 255])
            },}
        
    def find_creeper(self, bgr: np.ndarray, color: str) -> list:
        """
        Encontra o creeper na imagem com base na cor fornecida.
        
        Args:
            bgr (numpy.array): imagem no espaço de cor BGR.
            color (str): cor do creeper para identificação.

        Returns:
            list: lista de centros dos creepers detectados e a cor atual. No formato list( [(cx,cy), color], [...]... ).
        """
        creepers = []
        
        return creepers

    def distance(self, x1, x2):
        """
        Calcula a distância horizontal entre duas coordenadas.
        """
        distance = 0
        return distance

    def match_aruco(self, bgr, creepers, results):
        """
        Combina os marcadores Aruco com os creepers mais próximos.
        
        Args:
            bgr (numpy.array): imagem no espaço de cor BGR.
            creepers (list): lista de centros dos creepers detectados através da função `find_creeper`.
            results (list(dicts)): resultados da detecção Aruco.
                dict_keys(['id', 'rvec', 'tvec', 'distancia', 'corners', 'centro'])

        Returns:
            bgr (numpy.array): imagem com linhas desenhadas e pares combinados.
            matched_pairs (dict): detecções Aruco combinadas com o centro do "corpo" do creeper mais próximo, na chave "body_center".
            e a cor do creeper na chave "color". Remova creepers sem correspondência.
        """
        matched_pairs = []
        for creeper in creepers:
            
            # 3. Use a função sorted para ordenar os resultados por distância com base na função self.distance.
            closest = None 

            # 4. Remove da lista `results` o aruco mais próximo do corpo `creeper` para evitar que ele seja combinado novamente.

            # 5. Adiciona na variável o centro do creeper mais próximo na chave "body_center" do dicionário `closest`.
            # 6. Adiciona a cor do creeper mais próximo na chave "color" do dicionário `closest`.
            
            # 7. Desenha uma linha entre o centro do creeper e o centro do marcador Aruco.
            
            # 8. Adiciona o par combinado na lista `matched_pairs`.
        
        return bgr, matched_pairs

    def run(self, bgr):
        """
        Executa a detecção de Aruco e correspondência com creepers.
        
        Args:
            bgr (numpy.array): imagem no espaço de cor BGR.

        Returns:
            bgr (numpy.array): imagem no espaço de cor BGR com linhas desenhadas entre Arucos e creepers.
            ranked_arucos (list(dicts)): imagem processada e Arucos classificados por distância.
                dict_keys(['id', 'rvec', 'tvec', 'distancia', 'corners', 'centro', 'body_center', 'color'])
        """
        # 1. Chame a função self.detect_aruco e armazene os resultados em uma variável.
        _, results = None 
        
        creepers = []
        creepers += self.find_creeper(bgr, "green")
        creepers += self.find_creeper(bgr, "blue")

        # 2. Desenvolva a função `match_aruco` para combinar os marcadores Aruco com os corpos dos creepers.
        matched_pairs = None

        for result in matched_pairs:
            bgr = self.drawAruco(bgr, result)
            
        # 9. Utilize a função `sorted` para classificar os Arucos por distância.
        ranked_arucos = None

        return bgr, ranked_arucos
    

def rodar_webcam():
    Arucos = DistanceEstimator()
    # cap = cv2.VideoCapture(0) # webcam
    cap = cv2.VideoCapture('img/aruco.mp4') # Confira se o video esta na pasta img

    while True:
        ret, bgr = cap.read()
        bgr, ranked_arucos = Arucos.run(bgr)

        # 10. Imprime a distância e o id do creeper mais próximo da camera.

        cv2.imshow("Imagem", bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def rodar_frame():
    Arucos = DistanceEstimator()
    
    # bgr = cv2.imread("img/aruco.jpg")
    bgr = cv2.imread("img/aruco2.jpg")

    bgr, ranked_arucos = Arucos.run(bgr)
    cv2.imshow("Imagem", bgr)
    cv2.waitKey(0)

def main():
    # Selecione se deseja rodar seu codigo com uma imagem ou um video:
    # rodar_webcam()
    rodar_frame()


if __name__ == "__main__":
    main()