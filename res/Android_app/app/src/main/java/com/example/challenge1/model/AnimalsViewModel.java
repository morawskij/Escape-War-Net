package com.example.challenge1.model;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import java.util.ArrayList;
import java.util.List;

public class AnimalsViewModel extends ViewModel {

    private final MutableLiveData<List<Animal>> uiState =
            new MutableLiveData(new ArrayList<>());
    public LiveData<List<Animal>> getUiState() {
        return uiState;
    }
}
