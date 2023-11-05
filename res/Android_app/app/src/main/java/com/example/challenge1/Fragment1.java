package com.example.challenge1;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.res.Resources;
import android.net.Uri;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import com.example.challenge1.model.Animal;
import com.example.challenge1.model.AnimalsViewModel;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Fragment1 extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters

    //private String selectedAnimal = null;
    private String mParam1;
    private String mParam2;

    public Fragment1() {
        // Required empty public constructor
    }


    public static Fragment1 newInstance(String param1, String param2) {
        Fragment1 fragment = new Fragment1();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_1, container, false);
        Button button = view.findViewById(R.id.f1_button);
        button.setOnClickListener(v -> ((MainActivity) getActivity()).switchToFr2());

        AnimalsViewModel viewModel = new ViewModelProvider(requireActivity()).get(AnimalsViewModel.class);

        ImageView imageView = view.findViewById(R.id.imageView);

        List<String> myArraySpinner = new ArrayList<>();

        for (Animal a: viewModel.getUiState().getValue()){
            myArraySpinner.add(a.getName());
            System.out.println(a.getName());
        }

        @SuppressLint("CutPasteId") Spinner mySpinner;
        mySpinner = view.findViewById(R.id.spinner);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(getContext(), android.R.layout.simple_spinner_item, myArraySpinner);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        mySpinner.setAdapter(adapter);


        Spinner spin = view.findViewById(R.id.spinner);
        spin.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @SuppressLint("SetTextI18n")
            public void onItemSelected(AdapterView<?> spin, View v, int i, long id) {

                short temp;
                if(viewModel.getUiState().getValue().get(0).getName().equals(spin.getSelectedItem())) {
                    temp = 0;
                } else if (viewModel.getUiState().getValue().get(1).getName().equals((String) spin.getSelectedItem())){
                    temp = 1;
                } else {
                    temp = 2;
                }

                TextView result_x = view.findViewById(R.id.resultOwner);
                TextView result_y = view.findViewById(R.id.resultAge);


                result_x.setText("X: " + viewModel.getUiState().getValue().get(temp).getx());

                result_y.setText("Y: " + viewModel.getUiState().getValue().get(temp).gety());

                String res = (String) spin.getSelectedItem();
                Resources resources = getActivity().getResources();
                @SuppressLint("DiscouragedApi") final int resourceId = resources.getIdentifier(viewModel.getUiState().getValue().get(temp).getImage(), "drawable",
                        getActivity().getPackageName());
                imageView.setImageResource(resourceId);
//                selectedAnimal = spin.getSelectedItem().toString();
//                System.out.println(selectedAnimal);
                for (Animal a: viewModel.getUiState().getValue()){
                    a.setSelected(res.equals(a.getName()));
                }
                // set chosen to view-model

            }
            public void onNothingSelected(AdapterView<?> parent) {} // empty
        });



        return view;
    }



}