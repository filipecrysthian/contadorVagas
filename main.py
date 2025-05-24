import cv2
import pickle
import numpy as np

img = cv2.imread('media/estacionamento.png')

vagas = []


def capturar_vagas():
    for x in range(69):
        vaga = cv2.selectROI('vagas', img, False)
        cv2.destroyWindow('vagas')
        vagas.append(vaga)

        for x, y, w, h in vagas:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    with open('vagas.pkl', 'wb') as arquivo:
        pickle.dump(vagas, arquivo)


def contar_vagas():
    with open('vagas.pkl', 'rb') as arquivo:
        vagas = pickle.load(arquivo)
    video = cv2.VideoCapture('media/video.mp4')


    while True:
        check, img = video.read()
        img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_tr = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 25, 16)
        img_median = cv2.medianBlur(img_tr, 5)
        kernel = np.ones((3,3),np.int8)
        img_dilat = cv2.dilate(img_median, kernel)

        vagas_abertas = 0

        for x,y,w,h in vagas:
            vaga = img_dilat[y:y+h,x:x+w]
            cont = cv2.countNonZero(vaga)
            cv2.putText(img,str(cont), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,))

            if cont < 750:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                vagas_abertas +=1
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.rectangle(img, (90,0), (415,60),(0,255,0),-1)
            cv2.putText(img, f'LIVRE: {vagas_abertas}/69',(95,45), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (255,255,255), 5)

        cv2.imshow('video', img)
        cv2.waitKey(10)


contar_vagas()
