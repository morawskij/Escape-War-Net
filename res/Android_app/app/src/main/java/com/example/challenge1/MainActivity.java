package com.example.challenge1;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;

import com.example.challenge1.model.Animal;
import com.example.challenge1.model.AnimalsViewModel;

import java.util.Objects;


public class MainActivity extends AppCompatActivity {

    //protected AnimalsViewModel mViewModel = new ViewModelProvider(this).get(AnimalsViewModel.class)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        AnimalsViewModel model = new ViewModelProvider(this).get(AnimalsViewModel.class);
        populateAnimals(model);
        model.getUiState().observe(this, uiState -> {
            // update UI
        });
        getSupportFragmentManager().beginTransaction()
                .add(R.id.fragment_view, Fragment1.class, null)
                .commit(); // from activity - container

    }


    private void populateAnimals(AnimalsViewModel model){
        Objects.requireNonNull(model.getUiState().getValue()).add(new Animal(1, "Safe way to Escape", "31.356556", "1.214421", "icon1"));
        Objects.requireNonNull(model.getUiState().getValue()).add(new Animal(2, "Closest shelter", "31.356556", "", "icon1"));
        Objects.requireNonNull(model.getUiState().getValue()).add(new Animal(3, "Report danger", "42.4242420", "34.262917", "icon1"));

    }
    //31.358496054370935, 34.26625905017983
    public void locationOnStart(View view) {
        String locationCabras = "https://www.google.com/maps/dir/31%C2%B021'23.6%22N+34%C2%B015'46.5%22E/University+College+of+Applied+Sciences+of+Khan+Younis%D8%8C+%D8%A7%D9%84%D9%85%D9%88%D8%A7%D8%B5%D9%8A+-+%D8%AC%D9%86%D9%88%D8%A8+%D9%85%D8%B3%D8%AC%D8%AF+%D8%A7%D9%84%D9%82%D8%A8%D8%A9%D8%8C+%D8%AE%D8%A7%D9%86%D9%8A%D9%88%D9%86%D8%B3%E2%80%AD%E2%80%AD/@31.3549575,34.2611611,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x0:0x73640b8561db48ac!2m2!1d34.2629167!2d31.3565556!1m5!1m1!1s0x14fd90e5c5014c2d:0x83a95cd976e14c09!2m2!1d34.270834!2d31.3544417!3e2?entry=ttu";
        Intent webIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(locationCabras));
        startActivity(webIntent);
    }

    public void switchToFr2() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.fragment_view, Fragment2.class, null)
                .commit(); // from activity - container
    }
    public void switchToFr1() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.fragment_view, Fragment1.class, null)
                .commit(); // from activity - container
    }
}