package com.example.challenge1.model;

public class Animal {

    private Integer id;
    private String name;
    private String x;
    private String y;

    private final String image;

    private boolean selected;

    public boolean isSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }


    public Animal(Integer id, String name, String x, String y, String image) {
        this.id = id;
        this.name = name;
        this.x = x;
        this.y = y;
        this.image = image;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getx() {
        return x;
    }

    public void setx(String x) {
        this.x = x;
    }

    public String gety() {
        return y;
    }
    public void sety(String y) {
        this.y = y;
    }


    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getId() {
        return id;
    }

    public void setOwner(String y) {
        this.y = y;
    }

    public String getImage(){return image;}
}
