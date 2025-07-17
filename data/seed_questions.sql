-- Carga inicial de preguntas
-- Script SQL que podés ejecutar para agregar preguntas base a la tabla questions.
-- Ideal para poblar rápidamente la base en local o testing

INSERT INTO questions (role, question, correct_answer)
VALUES 
('Data Science', '¿Qué es overfitting?', 'Cuando un modelo aprende demasiado los datos de entrenamiento y no generaliza bien.'),
('Data Science', '¿Qué mide el ROC AUC?', 'La capacidad de un modelo de clasificación binaria para distinguir entre clases.');
-- Agregá más...
