#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:49:29 2024

@author: brooklynndominguez
"""

import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pizza Maker Game')
WHITE = (255, 255, 255)


pizza_base = pygame.image.load('pizza_base.png')
cheese = pygame.image.load('cheese.png')
pepperoni = pygame.image.load('pepperoni.png')
mushroom = pygame.image.load('mushroom.png')
olive = pygame.image.load('olive.png')
trashcan = pygame.image.load('trashcan.png')


pizza_base = pygame.transform.scale(pizza_base, (400, 400))
cheese = pygame.transform.scale(cheese, (100, 100))
pepperoni = pygame.transform.scale(pepperoni, (50, 50))
mushroom = pygame.transform.scale(mushroom, (50, 50))
olive = pygame.transform.scale(olive, (30, 30))
trashcan = pygame.transform.scale(trashcan, (200, 200))

ingredients = [
    {"name": "cheese", "image": cheese, "rect": cheese.get_rect(topleft=(50, 500))},
    {"name": "pepperoni", "image": pepperoni, "rect": pepperoni.get_rect(topleft=(200, 500))},
    {"name": "mushroom", "image": mushroom, "rect": mushroom.get_rect(topleft=(350, 500))},
    {"name": "olive", "image": olive, "rect": olive.get_rect(topleft=(500, 500))},
]

placed_toppings = []

pizza_rect = pizza_base.get_rect(center=(WIDTH // 2, HEIGHT // 2))
dragging = None
dragging_index = None
trashcan_rect = trashcan.get_rect(center=(WIDTH - 150, HEIGHT // 2))
running = True

while running:
    screen.fill(WHITE)
    screen.blit(pizza_base, pizza_rect)
    

    for ingredient in ingredients:
        screen.blit(ingredient["image"], ingredient["rect"])
        
    for topping in placed_toppings:
        screen.blit(topping["image"], topping["rect"])
        
    screen.blit(trashcan, trashcan_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
      
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos:
            for index, topping in enumerate(placed_toppings):
               if topping["rect"].collidepoint(event.pos):
                   dragging = topping
                   dragging_index = index
                   break
               
        if dragging is None and event.type == pygame.MOUSEBUTTONDOWN and event.pos:
            for ingredient in ingredients:
                if ingredient["rect"].collidepoint(event.pos):
                        dragging = {
                            "name": ingredient["name"],
                            "image": ingredient["image"],
                            "rect": ingredient["image"].get_rect(center=event.pos)  
                        }
                        dragging_index = None
                        break
                    
        if event.type == pygame.MOUSEBUTTONUP and event.pos:
            if dragging:
                if pizza_rect.colliderect(dragging["rect"]):
                    if dragging_index is not None:
                        placed_toppings[dragging_index] = dragging
                    else:
                        placed_toppings.append(dragging)
                trashcan_rect = trashcan.get_rect(center=(WIDTH - 150, HEIGHT // 2))  
                if trashcan_rect.colliderect(dragging["rect"]):
                    if dragging_index is not None:
                        placed_toppings.pop(dragging_index)
                    elif dragging in placed_toppings:
                        placed_toppings.remove(dragging)

            dragging = None
            dragging_index = None
        
        
      
        if event.type == pygame.MOUSEMOTION and event.pos:
            if dragging:
                dragging["rect"].center = event.pos
    
    if dragging:
        screen.blit(dragging["image"], dragging["rect"])
    pygame.display.flip()


pygame.quit()
sys.exit()